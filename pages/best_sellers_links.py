from selenium.webdriver.common.by import By
from pages.base_page import Page

class BestSellers(Page):
    HEADER_LINK = (By.CSS_SELECTOR, '#zg_header a')

    def verify_headers_links(self, expected_amount):
        expected_amount = int(expected_amount)
        links = self.find_elements(*self.HEADER_LINK)
        assert len(links) == expected_amount, f'Expected {expected_amount}links but got {len(links)}'