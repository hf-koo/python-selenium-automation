from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Best_Sellers = (By.CSS_SELECTOR, 'a[href*="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
Customer_Service = (By.CSS_SELECTOR, 'a[href*="/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice"]')
Header_Link = (By.CSS_SELECTOR, '#zg_header a')
Issue_Card = (By.CSS_SELECTOR, '.issue-card-wrapper')
Nav_Orders = (By.ID, 'nav-orders')
@given("Open Amazon page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on orders')
def click_on_shopping_cart_icon(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(Nav_Orders),
        message='Nav Orders not clickable'
    ).click()


@when('Click on best sellers')
def best_sellers(context):
    context.driver.find_element(*Best_Sellers).click()


@when('Click on customer service')
def customer_services(context):
    context.driver.find_element(*Customer_Service).click()


@then('Verify sign in text is correct')
def verify_cart_result(context):
    expect_result = 'Sign in'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-box-inner .a-spacing-small').text
    assert expect_result in actual_result, f'Error, expected {expect_result} did not match actual {actual_result}'


@then('Verify header has {expected_amount}links')
def verify_un_order_list(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*Header_Link)
    assert len(links) == expected_amount, f'Expected {expected_amount}links but got {len(links)}'


@then('Verify issue card has {expected_amount}')
def verify_issue_card(context, expected_amount):
    links = context.driver.find_elements(*Issue_Card)
    assert len(links) > 1, f'Expected at least 11 links, but got {len(links)}'