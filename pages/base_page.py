from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger
from time import sleep

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, end_url=''):
        url = f'https://www.amazon.com/{end_url}'
        self.driver.get(url)
        logger.info(f'Openning URL {url}')
        sleep(2)
        self.driver.refresh()

    def click(self, *locator):
        logger.info(f'Clicking on {locator}')
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        logger.info(f'Searching for {locator}')
        return self.driver.find_element(*locator)

    def input_text(self, text: str, *locator):
        e = self.find_element(*locator)
        logger.info(f'Inputting text: "{text}"')
        e.send_keys(text)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text in expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Error, expected partial text {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_part_of_url):
        self.wait.until(EC.url_contains(expected_part_of_url))

    def verify_texts(self, expected_amount, *locator):
        actual_amount = self.find_elements(*locator)
        expected_amount = int(expected_amount)
        actual_amount = len(actual_amount)
        # links = self.find_elements(*self.HEADER_LINK)
        assert expected_amount == actual_amount, \
            f'Expected {expected_amount}links but got {actual_amount}'

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_windows(self):
        windows = self.driver.window_handles
        print(windows)
        return windows

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(all_windows)
        print(f'Switching to {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window(self, window_id):
        print(f'Switching to {window_id}')
        self.driver.switch_to.window(window_id)

    def close_page(self):
        self.driver.close()

    def wait_for_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable: {locator}'
        )

    def wait_for_element_clickable_click(self, *locator):
        e = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable: {locator}'
        )
        e.click()

    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element did not appear: {locator}'
        )

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element did not disappear: {locator}'
        )
