import time

from conftest import driver
from pages.report_constructor_page import ReportConstructorPage
from pages.login_page import LoginPage



class Test_Auth:
    def test_positive_login (self, driver):
                login_page = LoginPage(driver, "http://localhost:4200/")
                login_page.open()
                login_page.login_and_password_input()
                login_page.get_output_result()
                assert login_page.get_output_result() == 'Никитин (Тестовый) Павел Сергеевич'
                time.sleep(3)








