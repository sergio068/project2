import unittest
from myapp.models import Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):

    def test_read_product(self):
        product = ProductFactory()
        self.assertIsNotNone(product.id)

    def test_update_product(self):
        product = ProductFactory()
        product.name = "Updated Name"
        self.assertEqual(product.name, "Updated Name")

    def test_delete_product(self):
        product = ProductFactory()
        product.delete()
        self.assertIsNone(Product.query.get(product.id))

    def test_list_all_products(self):
        products = Product.query.all()
        self.assertGreater(len(products), 0)

    def test_find_by_name(self):
        product = ProductFactory(name="UniqueName")
        found = Product.find_by_name("UniqueName")
        self.assertEqual(found.name, "UniqueName")

    def test_find_by_category(self):
        product = ProductFactory(category="Electronics")
        found = Product.find_by_category("Electronics")
        self.assertEqual(found.category, "Electronics")

    def test_find_by_availability(self):
        product = ProductFactory(available=True)
        found = Product.find_by_availability(True)
        self.assertTrue(found.available)

