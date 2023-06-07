from selenium.webdriver.common.by import By


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
