from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class TCPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0]')
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


