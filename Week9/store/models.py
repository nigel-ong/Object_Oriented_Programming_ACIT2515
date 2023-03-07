from database import db


class Product(db.Model):
    name = db.Column(db.String, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        product_dict = {"name": self.name,"price": self.price,"quantity": self.quantity}
        return product_dict

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    products = db.relationship('ProductsOrder', back_populates='order')

    def to_dict(self):
        pro_dict = []
        price = 0
        for product in self.products:
            pro_dict.append({"name": product.product.name,"quantity": product.quantity})
            price += product.quantity * product.product.price

        order_dict = {
            "customer_name":self.name,
            "customer_address":self.address,
            "products": pro_dict,
            "price": round(price,2)
        }
        return order_dict

class ProductsOrder(db.Model):
    product_name = db.Column(db.ForeignKey("product.name"), primary_key =True)
    order_id = db.Column(db.ForeignKey("order.id"), primary_key =True)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product')
    order = db.relationship('Order', back_populates='products')
