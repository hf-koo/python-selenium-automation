from selenium.webdriver.common.by import By
from pages.base_page import Page

class ShoppingCart(Page):

    SHOPCART = (By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty')
    CART = (By.ID, 'nav-cart-count-container')

    def click_cart(self):
        self.click(*self.CART)

    def verify_empty_cart(self, expected_result):
         self.verify_text(expected_result, *self.SHOPCART)


