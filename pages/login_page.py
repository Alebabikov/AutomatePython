from locators.locators import LoginPageLocators
from locators.locators import HeaderPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def login_and_password_input(self):
        self.element_is_visible(LoginPageLocators.LOGIN_FIELD).click()
        self.element_is_visible(LoginPageLocators.LOGIN_FIELD).send_keys('ad')
        self.element_is_visible(LoginPageLocators.PASSWORD_FIELD).click()
        self.element_is_visible(LoginPageLocators.PASSWORD_FIELD).send_keys('ad')
        self.element_is_visible(LoginPageLocators.BTN_LOGIN).click()

    def get_output_result(self):
        return self.element_is_present(HeaderPageLocators.USER_PROFILE).text



