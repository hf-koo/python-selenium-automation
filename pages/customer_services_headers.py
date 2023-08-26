from selenium.webdriver.common.by import By
from pages.base_page import Page

class CustomerServices(Page):


    ISSUE_CARD = (By.CSS_SELECTOR, '.issue-card-wrapper')

    def verify_issue_cards(self, expected_amount):
        links = self.find_elements(*self.ISSUE_CARD)
        assert len(links) >= int(expected_amount), f'Expected at least 11 links, but got {len(links)}'