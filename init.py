import os.path
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect, Blueprint
from views import *
from conf import config

ACTIVE_ENDPOINTS = [('/cart', cart), ('/categories', categories)]
app = Flask(__name__, static_url_path="/static", static_folder='static')

dir_folder = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(dir_folder, "pharmasy.db"))
config = config.DevelopmentConfig
app.config.from_object(config)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
for url, blueprint in ACTIVE_ENDPOINTS:
     app.register_blueprint(blueprint, url_prefix=url)
db = SQLAlchemy(app)

class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    inventorys = db.relationship('Inventory', backref='zone', lazy='select')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    products = db.relationship('Product', backref='category', lazy='select')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)

class Client(db.Model):
    id_type = db.Column(db.String(20), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True, unique=True)
    address = db.Column(db.String(80), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    types_id = db.relationship('Order', backref='types_id', lazy='select')
    ids = db.relationship('Order', backref='ids', lazy='select')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('client.id_type'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    creation_date = db.Column(db.Date, nullable=False)
    deliver_date = db.Column(db.Date, nullable=False)
    total_value = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(30), nullable=False)
    items = db.relationship('Item', backref='order', lazy='select')

class Inventory(db.Model):
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price_unitary = db.Column(db.Float, nullable=False)
    items = db.relationship('Item', backref='Inventory', lazy='select')

class Item(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.Integer, db.ForeignKey('inventory.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Funciones CRUD
def create_zone(name):
    zone = Zone(name)
    db.session.add(zone)
    db.session.commit()
    db.session.refresh(zone)

# def read_subjects():
#     return db.session.query(Subject).all()
#
#
# def update_subject(subject_id, name):
#     db.session.query(Subject).filter_by(id=subject_id).update({
#         "nom": name
#     })
#     db.session.commit()
#
#
# def delete_subject(subject_id):
#     db.session.query(Subject).filter_by(id=subject_id).delete()
#     db.session.commit()

@app.route("/", methods=["GET"])
def show_product():
    create_zone('Centro')
    return render_template('cart.html')


if __name__ == "__main__":
    db.create_all()
    app.run()