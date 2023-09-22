from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Amazon page")
def open_amazon(context):
    context.app.main_page.open_main()


@given("Open Amazon T&C page")
def open_amazon_t_c(context):
    context.app.t_c_page.open_t_c()


@when('Click on orders')
def click_on_shopping_cart_icon(context):
    context.app.header.click_signin_popup()


@when('Click on best sellers')
def best_sellers(context):
    context.app.header.search_best_sellers()


@when('Click on customer service')
def customer_services(context):
    context.app.header.search_customer_services()


@when('Click on shopping cart icon')
def click_on_shopping_cart_icon(context):
    context.app.shopping_cart.click_cart()


@when('Store original windows')
def store_org_win(context):
    context.original_window = context.app.t_c_page.store_original_window()


@when('Click on Amazon Privacy Notice')
def open_privacy_notice(context):
    context.app.t_c_page.open_privacy_notice()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.t_c_page.switch_to_newer_window()


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select Cell phones & Accessories')
def select_dept(context):
    context.app.header.select_dept()


@when('Search for {text}')
def word_search(context, text):
    context.app.header.search_iphone(text)


@then('Verify sign in text is {expected_result}')
def verify_sign_in_result(context, expected_result):
    context.app.sign_in_page.verify_signin_opened(expected_result)


@then('Verify header has {expected_amount}links')
def verify_headers_link(context, expected_amount):
    context.app.best_sellers.verify_headers_links(expected_amount)


@then('Verify issue card has {expected_amount}')
def verify_issue_card(context, expected_amount):
    context.app.customer_services.verify_issue_cards(expected_amount)


@then('Verify cart result is {result}')
def verify_cart_result(context, result):
    context.app.shopping_cart.verify_empty_cart(result)


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_notice(context):
    context.app.t_c_page.verify_privacy_open()


@then('User can close new window')
def user_can_close_new_window(context):
    context.app.t_c_page.user_can_close_new_window()


@then('Switch back to original')
def user_switch_back_original(context):
    context.app.base_page.switch_to_window(context.original_window)


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()


@then('Verify Cell phones department selected')
def verify_dept_selected(context):
    context.app.header.verify_dept_selected()
    sleep(4)
