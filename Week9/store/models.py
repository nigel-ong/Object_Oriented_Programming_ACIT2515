from database import db


class Product(db.Model):
    name = db.Column(db.String, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        product_dict = {"name": self.name,"price": self.price,"quantity": self.quantity}
        return product_dict