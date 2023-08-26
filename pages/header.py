from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    NAV_ORDERS = (By.ID, 'nav-orders')
    BEST_SELLERS = (By.CSS_SELECTOR, 'a[href*="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
    CUSTOMER_SERVICES = (By.CSS_SELECTOR, 'a[href*="/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice"]')


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)


    def click_sigin_popup(self, *locator):
        self.click(*self.NAV_ORDERS)


    def search_best_sellers(self):
        self.click(*self.BEST_SELLERS)


    def search_customer_services(self):
        self.click(*self.CUSTOMER_SERVICES)