from behave import when, then
from myapp import app

@when('I get the product with id {id}')
def step_impl(context, id):
    response = context.client.get(f'/products/{id}')
    context.response = response

@when('I update the product with id {id}')
def step_impl(context, id):
    product_data = {row['key']: row['value'] for row in context.table}
    response = context.client.put(f'/products/{id}', json=product_data)
    context.response = response

@when('I delete the product with id {id}')
def step_impl(context, id):
    response = context.client.delete(f'/products/{id}')
    context.response = response

@when('I list all products')
def step_impl(context):
    response = context.client.get('/products')
    context.response = response

@when('I search for products with name "{name}"')
def step_impl(context, name):
    response = context.client.get(f'/products?name={name}')
    context.response = response

@when('I search for products with category "{category}"')
def step_impl(context, category):
    response = context.client.get(f'/products?category={category}')
    context.response = response

@when('I search for products with availability "{availability}"')
def step_impl(context, availability):
    response = context.client.get(f'/products?available={availability}')
    context.response = response

@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)

@then('the response should contain "{text}"')
def step_impl(context, text):
    assert text in context.response.get_data(as_text=True)

@then('the response should contain {count} products')
def step_impl(context, count):
    data = context.response.get_json()
    assert len(data) == int(count)

