import time
import pytest
from Pages.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver_init")  # 👈 This connects your driver setup to the class
class TestValidateCodeLogic:

    def test_validate_code_logic(self, driver_init):
        #login=LoginPage(self.driver)
        # Initialize the driver if not already done by the fixture
        # from selenium import webdriver
        # self.driver = webdriver.Chrome()
        driver=driver_init
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        """
        driver.get("https://www.facebook.com/")
        #login = LoginPage(self.driver)
        driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
        time.sleep(3)

        gender_radio_buttons = driver.find_elements(By.XPATH, "//input[@name='sex']")
        print(f"Radio buttons available for gender selection: {len(gender_radio_buttons)}")

        for i, radio in enumerate(gender_radio_buttons, start=1):
            print(f"Radio {i}: value={radio.get_attribute('value')}")

        for radio in gender_radio_buttons:
            radio.click()
            time.sleep(2)
            selected_values = [r.get_attribute('value') for r in gender_radio_buttons if r.is_selected()]
            print(f"Selected value after clicking: {selected_values}")
            assert len(selected_values) == 1, "More than one radio button is selected!"
        """

    