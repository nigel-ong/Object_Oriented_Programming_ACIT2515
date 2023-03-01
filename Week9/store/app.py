from pathlib import Path

from flask import Flask, jsonify, render_template, request

from database import db
from models import Product

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)


@app.route("/")
def home():
    data = Product.query.all()
    return render_template("index.html", products=data)


@app.route("/api/product/<string:name>", methods=["GET"])
def api_get_product(name):
    product = db.session.get(Product, name.lower())
    product_json = product.to_dict()
    return jsonify(product_json)


@app.route("/api/product", methods=["POST"])
def api_create_product():
    data = request.json
    # Check all data is provided
    for key in ("name", "price", "quantity"):
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400

    try:
        price = float(data["price"])
        quantity = int(data["quantity"])
        # Make sure they are positive
        if price < 0 or quantity < 0:
            raise ValueError
    except ValueError:
        return (
            "Invalid values: price must be a positive float and quantity a positive integer",
            400,
        )

    product = Product(
        name=data["name"],
        price=price,
        quantity=quantity,
    )
    db.session.add(product)
    db.session.commit()
    return "Item added to the database"

@app.route("/api/product/<string:name>", methods=["DELETE"])
def api_delete_product(name):
    product = db.session.get(Product, name.lower())
    db.session.delete(product)
    db.session.commit()
    return "Deleted"

@app.route("/api/product/<string:name>", methods=["PUT"])
def api_put_product(name):
    data = request.json
    product = db.session.get(Product, name.lower())
    if "price" in data.keys():
        product.price = data["price"]
    else:
        product.price = product.price
    # if "quantity" in data.keys():
    #     product.quantity = data["quantity"]

    # if data.quantity in data:
    #     product.quantity = data["quantity"]
    # else:
    #     product.quantity = product.quantity 

    # try:
    #     if not isinstance(data["quantity"],int) or int(data["quantity"]) < 0:
    #         raise AttributeError
    #     elif not isinstance(data["price"],float) or float(data["price"]) < 0:
    #         raise ValueError
    # except ValueError:
    #     return (
    #         "Invalid float values: price must be a positive or float",
    #         400,
    #     )
    # except AttributeError:
    #     return (
    #         "Invalid int values: Not an positive or integer",
    #         400,
    #     )
    db.session.add(product)
    db.session.commit()
    return "Updated"

if __name__ == "__main__":
    app.run(debug=True)
