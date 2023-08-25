from selenium.webdriver.common.by import By
from pages.base_page import Page

class Order(Page):
    NAV_ORDERS = (By.ID, 'nav-orders')
    # ORDERS = (By.ID, 'nav-cart-count-container')


    def click_sigin_popup(self, *locator):
        self.click(*self.NAV_ORDERS)
