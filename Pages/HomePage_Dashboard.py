from Pages.PatientsPage import PatientsPage
from Utils.LocatorReader import LocatorReader
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import Config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HomePage_Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator_reader = LocatorReader()

        self.HOME_PAGE_TAB_LOCATOR = (By.XPATH, self.locator_reader.get("dashboard_home_page", "dashboard_tab"))
        self.PATIENTS_TAB_LOCATOR = (By.XPATH, self.locator_reader.get("dashboard_home_page", "patients_tab"))
        self.PATIENTS_ICON_LOCATOR = (By.XPATH, self.locator_reader.get("dashboard_home_page", "patientsIcon_tab"))

    def verify_home_page_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.HOME_PAGE_TAB_LOCATOR))
            home_tab_text=self.get_text(self.HOME_PAGE_TAB_LOCATOR)
            print(f"Home page loaded successfully: {home_tab_text}")
            return True
        except Exception as e:
            print(f"Home page did not load: {e}")
            return False

    def navigate_patients_tab(self):
        self.wait_and_click(self.PATIENTS_TAB_LOCATOR)
        return PatientsPage(self.driver).verify_patient_page_loaded()