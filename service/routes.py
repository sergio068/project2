from flask import Flask, jsonify, request
from myapp.models import Product

app = Flask(__name__)

@app.route('/products/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.serialize())

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    product.update(request.json)
    return jsonify(product.serialize())

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    product.delete()
    return '', 204

@app.route('/products', methods=['GET'])
def list_all_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products])

@app.route('/products', methods=['GET'])
def find_by_name():
    name = request.args.get('name')
    product = Product.query.filter_by(name=name).first_or_404()
    return jsonify(product.serialize())

@app.route('/products', methods=['GET'])
def find_by_category():
    category = request.args.get('category')
    products = Product.query.filter_by(category=category).all()
    return jsonify([product.serialize() for product in products])

@app.route('/products', methods=['GET'])
def find_by_availability():
    available = request.args.get('available')
    products = Product.query.filter_by(available=available).all()
    return jsonify([product.serialize() for product in products])

