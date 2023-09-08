from pages.main_page import MainPage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.best_sellers_links import BestSellers
from pages.customer_services_headers import CustomerServices
from pages.shopping_cart import ShoppingCart
from pages.t_c_page import TCPage

class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.shopping_cart = ShoppingCart(driver)
        self.sign_in_page = SignInPage(driver)
        self.best_sellers = BestSellers(driver)
        self.customer_services = CustomerServices(driver)
        self.t_c_page = TCPage(driver)
