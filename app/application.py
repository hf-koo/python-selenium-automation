from pages.main_page import MainPage
from pages.header import Header
from pages.order import Order
from pages.sign_in_page import SignInPage
class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)

        self.main_page = MainPage(driver)
        self.order = Order(driver)
        self.sign_in_page = SignInPage(driver)