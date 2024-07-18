import unittest
from myapp import app
from myapp.models import Product
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_read_product(self):
        product = ProductFactory()
        response = self.app.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        product = ProductFactory()
        response = self.app.put(f'/products/{product.id}', json={'name': 'Updated Name'})
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        product = ProductFactory()
        response = self.app.delete(f'/products/{product.id}')
        self.assertEqual(response.status_code, 204)

    def test_list_all_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_find_by_name(self):
        product = ProductFactory(name="UniqueName")
        response = self.app.get('/products?name=UniqueName')
        self.assertEqual(response.status_code, 200)

    def test_find_by_category(self):
        product = ProductFactory(category="Electronics")
        response = self.app.get('/products?category=Electronics')
        self.assertEqual(response.status_code, 200)

    def test_find_by_availability(self):
        product = ProductFactory(available=True)
        response = self.app.get('/products?available=True')
        self.assertEqual(response.status_code, 200)

