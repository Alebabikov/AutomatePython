import time

from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators.form_page_locators import FormPageLocators as Locators

class FormPage(BasePage):

    def fill_fields_and_submit(self):
        search_field = 'ololol'


        self.element_is_visible(Locators.SEARCH_FIELD).click()
        self.element_is_visible(Locators.SEARCH_FIELD).send_keys(search_field)
        self.element_is_visible(Locators.SEARCH_FIELD).send_keys(Keys.RETURN)
        time.sleep(3)

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)