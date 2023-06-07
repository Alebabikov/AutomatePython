from selenium.webdriver.common.by import By


class FormPageLocators:
    LOGIN_FIELD = (By.XPATH, "//input[@name='userName']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    BTN_LOGIN = (By.XPATH, "//span[text()='Log in']")

    CREATED_LOGIN = (By.XPATH, "//input[@ng-reflect-model='ad']")
    CREATED_PASSWORD = (By.XPATH, "//input[@ng-reflect-model='ad']")