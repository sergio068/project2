from factory import Factory, Faker
from myapp.models import Product

class ProductFactory(Factory):
    class Meta:
        model = Product

    name = Faker('word')
    category = Faker('word')
    available = Faker('boolean')
    price = Faker('random_number', digits=5)

