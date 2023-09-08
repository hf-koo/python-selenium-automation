from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class TCPage(Page):

    PRIVACY_NOTICE = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')

    def open_t_c(self):
        self.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
        sleep(2)
        self.driver.refresh()

    def open_privacy_notice(self):
        self.click(*self.PRIVACY_NOTICE)

    def store_original_window(self):
        return self.get_current_window()

    def switch_to_newer_window(self):
        self.switch_to_new_window()

    def verify_privacy_open(self):
        self.verify_partial_url('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ')

    def user_can_close_new_window(self):
        self.close_page()

    # def user_can_return_original_window(self):
    #     self.switch_to_window(self, *self.window_id)





