from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Open Amazon")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on shopping cart icon')
def click_on_shopping_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@then('Verify cart result is empty')
def verify_cart_result(context):
    expect_result = '0'
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert expect_result in actual_result, f'Error, expected {expect_result} did not match actual {actual_result}'

