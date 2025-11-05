import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.LocatorReader import LocatorReader
import os
from Utils.Excel_Reader import ExcelReader
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator_reader = LocatorReader()

        self.EMAIL_LOCATOR = (By.XPATH, self.locator_reader.get(
            "login_page", "username_input"))
        self.PASSWORD_LOCATOR = (By.XPATH, self.locator_reader.get(
            "login_page", "password_input"))
        self.LOGIN_BUTTON_LOCATOR = (
            By.XPATH, self.locator_reader.get("login_page", "login_button"))

    def login(self):

        if Config.ENV == "QA":
            url = Config.QA_URL
            username = Config.USERNAME
            password = Config.QA_PASSWORD

        elif Config.ENV == "UAT":
            url = Config.UAT_URL
            username = Config.USERNAME
            password = Config.UAT_PASSWORD
        else:
            raise ValueError("Invalid environment")

        self.driver.get(url)
        self.wait_and_click(self.EMAIL_LOCATOR)
        self.enter_text(self.EMAIL_LOCATOR, username)
        self.enter_text(self.PASSWORD_LOCATOR, password)
        self.wait_and_click(self.LOGIN_BUTTON_LOCATOR, test_name="LoginTest")
        time.sleep(3)
