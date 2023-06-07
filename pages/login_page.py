import time

from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators.login_page_locators import FormPageLocators as Locators

class LoginPage(BasePage):

    def login_and_password_input(self):
        self.element_is_visible(Locators.LOGIN_FIELD).click()
        self.element_is_visible(Locators.LOGIN_FIELD).send_keys('ad')
        self.element_is_visible(Locators.PASSWORD_FIELD).click()
        self.element_is_visible(Locators.PASSWORD_FIELD).send_keys('ad')
        self.element_is_visible(Locators.BTN_LOGIN).click()

   # def check_login_and_password_input(self):
    #    login = self.elements_is_present(Locators.CREATED_LOGIN).text
     #   password = self.elements_is_present(Locators.CREATED_PASSWORD).text
      #  return login, password



