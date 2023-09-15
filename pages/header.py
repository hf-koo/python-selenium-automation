
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    NAV_ORDERS = (By.ID, 'nav-orders')
    BEST_SELLERS = (By.CSS_SELECTOR, 'a[href*="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
    CUSTOMER_SERVICES = (By.CSS_SELECTOR, 'a[href*="/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice"]')
    LANG_SELECTION = (By.CSS_SELECTOR, ".icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href="#switch-lang=es_US"]')
    DEPT_SELECTION = (By.ID, 'searchDropdownBox')
    SUBHEADER_DEPT = (By.XPATH, "//option[@selected='selected' and @value='search-alias=mobile']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)


    def click_signin_popup(self, *locator):
        self.click(*self.NAV_ORDERS)


    def search_best_sellers(self):
        self.click(*self.BEST_SELLERS)


    def search_customer_services(self):
        self.click(*self.CUSTOMER_SERVICES)

    def hover_lang(self):
        actions = ActionChains(self.driver)
        lang = self.find_element(*self.LANG_SELECTION)
        actions.move_to_element(lang)
        actions.perform()


    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)


    def select_dept(self):
        dept_selection = self.find_element(*self.DEPT_SELECTION)
        select = Select(dept_selection)
        select.select_by_value('search-alias=mobile')

    def search_iphone(self, text):
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)


    def verify_dept_selected(self):
        self.wait_for_element_appear(*self.SUBHEADER_DEPT)

