import time

from conftest import driver
from pages.login_page import BasePage, LoginPage


class TestAuth:
    class TestPositiveLogin:
        def test_positive_login (self, driver):
            login_page = LoginPage(driver, 'http://localhost:4200/')
            login_page.open()
            login_page.login_and_password_input()


        #    output_login, output_password = login_page.check_login_and_password_input()
        #   print(output_login)
        #    print(output_password)

            time.sleep(5)



