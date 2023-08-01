from selenium.webdriver.common.by import By
from behave import given, when, then

@given("Open Amazon page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

# @when('Click on sign in')
# def click_account_list(context):
#     context.driver.find_element(By.ID, 'nav_ya_signin').click()

@when('Click on orders')
def click_on_shopping_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify sign in text is correct')
def verify_cart_result(context):
    expect_result = 'Sign in'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-box-inner .a-spacing-small').text
    assert expect_result in actual_result, f'Error, expected {expect_result} did not match actual {actual_result}'