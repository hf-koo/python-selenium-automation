from selenium.webdriver.common.by import By
from behave import given, when, then







@given("Open Amazon page")
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Click on orders')
def click_on_shopping_cart_icon(context):
    context.app.header.click_sigin_popup()


@when('Click on best sellers')
def best_sellers(context):
    context.app.header.search_best_sellers()


@when('Click on customer service')
def customer_services(context):
    context.app.header.search_customer_services()


@then('Verify sign in text is {expected_result}')
def verify_sign_in_result(context, expected_result):
# expect_result = 'Sign in'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-box-inner .a-spacing-small').text
#     assert expect_result in actual_result, f'Error, expected {expect_result} did not match actual {actual_result}'
    context.app.sign_in_page.sign_in_result(expected_result)

@then('Verify header has {expected_amount}links')
def verify_headers_link(context, expected_amount):
    # expected_amount = int(expected_amount)
    # links = context.driver.find_elements(*Header_Link)
    # assert len(links) == expected_amount, f'Expected {expected_amount}links but got {len(links)}'
    context.app.best_sellers.verify_headers_links(expected_amount)


@then('Verify issue card has {expected_amount}')
def verify_issue_card(context, expected_amount):
    #links = context.driver.find_elements(*Issue_Card)
    #assert len(links) > 1, f'Expected at least 11 links, but got {len(links)}'
    context.app.customer_services.verify_issue_cards(expected_amount)