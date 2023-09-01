from selenium.webdriver.common.by import By
from pages.base_page import Page

class BestSellers(Page):
    HEADER_LINK = (By.CSS_SELECTOR, '#zg_header a')

    def verify_headers_links(self, expected_amount):

        self.verify_texts(expected_amount, *self.HEADER_LINK)