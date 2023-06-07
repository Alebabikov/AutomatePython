import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():

    options = Options()
    options.set_capability("acceptInsecureCerts", True)

    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    yield driver
    driver.quit()