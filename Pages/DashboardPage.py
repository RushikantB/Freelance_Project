import time
from Pages.BasePage import BasePage
from Utils.LocatorReader import LocatorReader
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator_reader = LocatorReader()

        self.TIMEATWORKHEADER_LOCATOR = (
            By.XPATH, self.locator_reader.get("dashboard_page", "time_at_work_header"))
        self.MYACTIONHEADER_LOCATOR = (
            By.XPATH, self.locator_reader.get("dashboard_page", "my_actions_header"))
        self.ADMINLINK_LOCATOR = (
            By.XPATH, self.locator_reader.get("menu_panel", "admin_link"))
        self.RECRUITMENTLINK_LOCATOR = (
            By.XPATH, self.locator_reader.get("menu_panel", "recruitment_link"))

    def verify_dashboard_headers(self):
        txt_timeatwork = self.get_text(self.TIMEATWORKHEADER_LOCATOR)
        print(txt_timeatwork)

        txt_myactionsheader = self.get_text(self.MYACTIONHEADER_LOCATOR)
        print(txt_myactionsheader)

    def click_on_admin_link(self):
        self.wait_and_click(self.ADMINLINK_LOCATOR)
        time.sleep(5)

    def click_on_recruitment_link(self):
        self.wait_and_click(self.RECRUITMENTLINK_LOCATOR)
        self.wait_for_page_to_load()

    