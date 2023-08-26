from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-box-inner .a-spacing-small')
    expected_text = 'Sign in'

    def sign_in_result(self, expected_text):
        actual_text = self.find_element(*self.SEARCH_RESULT).text

        assert actual_text == expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'