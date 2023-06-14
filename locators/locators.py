from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, "//input[@name='userName']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    BTN_LOGIN = (By.XPATH, "//span[text()='Log in']")

class HeaderPageLocators:
    USER_PROFILE = (By.XPATH, "//div[text()=' Никитин (Тестовый) Павел Сергеевич ']")
    BTN_CALENDAR = (By.XPATH, "//button[@mattooltip='Календарь событий']")
    BTN_MESSAGE = (By.XPATH, "//button[@mattooltip='Центр сообщений']")
    BTN_EVENT = (By.XPATH, "//button[@mattooltip='События']")
    BTN_EXIT = (By.XPATH, "//button[@mattooltip='Выход']")

class FormPageLocators:
    BTN_MENU = (By.XPATH, "//mat-icon[text()='menu']")
    BTN_ADM = (By.XPATH, "//span[text()='Администрирование ']")
    BTN_CITYPOINT = (By.XPATH, "//span[text()='CityPoint ']")
    BTN_DASHBOARD = (By.XPATH, "//span[text()='Dashboard ']")
    BTN_REPORTS = (By.XPATH, "//span[text()='Отчеты ']")
    BTN_LPU = (By.XPATH, "//span[text()='Учреждения ']")
    BTN_DOCTORS = (By.XPATH, "//span[text()='Врачи ']")
    BTN_REPRESENTATIONS = (By.XPATH, "//span[text()='Представительства ']")
    BTN_TERRITORY = (By.XPATH, "//span[text()='Территории ']")
    BTN_TERRITORIES_BY_STATE = (By.XPATH, "//span[text()='Территории по штату ']")
    BTN_USERS = (By.XPATH, "//span[text()='Пользователи ']")
    BTN_PLANNER = (By.XPATH, "//span[text()='Планировщик ']")
    BTN_PRESENTATION = (By.XPATH, "//span[text()='Презентации ']")
    BTN_ROUTE_SHEET = (By.XPATH, "//span[text()='Маршрутные листы ']")
    BTN_EVENT_REGISTRATION = (By.XPATH, "//span[text()='Лог регистрации событий  ']")

class SelectionReportsPageLocators:
    BTN_REPORTS_WITH_OUT_A_GROUP = (By.XPATH, "//span[text()='Без группы ']")
    BTN_DOUBLE_VISITS = (By.XPATH, "//mat-card-title[text()='Двойные визиты']")

class ConstructorReportsPageLocators:
    BTN_CHEVRON = (By.XPATH, "//button[@aria-label='toggle undefined']")


