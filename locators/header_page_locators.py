from selenium.webdriver.common.by import By


class FormPageLocators:
    USER_PROFILE = (By.XPATH, "//div[text()=' Никитин (Тестовый) Павел Сергеевич ']")
    BTN_CALENDAR = (By.XPATH, "//button[@mattooltip='Календарь событий']")
    BTN_MESSAGE = (By.XPATH, "//button[@mattooltip='Центр сообщений']")
    BTN_EVENT = (By.XPATH, "//button[@mattooltip='События']")
    BTN_EXIT = (By.XPATH, "//button[@mattooltip='Выход']")
