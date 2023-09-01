from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")


    def verify_signin_opened(self, expected_result):
        self.verify_text(expected_result, *self.SIGNIN_HEADER)
