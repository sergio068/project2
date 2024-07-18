from behave import given
from myapp import db
from myapp.models import Product

@given('the following products')
def step_impl(context):
    for row in context.table:
        product = Product(
            name=row['name'],
            category=row['category'],
            available=row['available'] == 'True',
            price=row['price']
        )
        db.session.add(product)
    db.session.commit()
 
