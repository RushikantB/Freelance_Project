from datetime import datetime
import time
from Pages.BasePage import BasePage
from Utils.Excel_Reader import ExcelReader
from Utils.LocatorReader import LocatorReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PatientDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        self.locator_reader=LocatorReader()
        self.reader=ExcelReader()

        self.PATIENT_HEADER_LOCATOR = (By.XPATH, self.locator_reader.get("patient_details_page","patientname_header"))
        self.CLOSE_PATIENT_DETAILS_TAB_LOCATOR = (By.XPATH, self.locator_reader.get("patient_details_page","close_patient_details_page"))
        self.ADD_ENCOUNTER_BUTTON_LOCATOR = (By.XPATH, self.locator_reader.get("patient_details_page","add_encounter_button")) 
        
    def get_patient_name(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.PATIENT_HEADER_LOCATOR)
        )
        full_text = element.text.strip()  
        name_part = full_text.split("(")[0].strip()
        parts = [x.strip() for x in name_part.split(",")]
        last_name = parts[0]  
        first_name = parts[1].split('"')[0].strip()  
        return first_name.lower(), last_name.lower()  
    
    def close_patient_details_tab(self):
        #element = self.wait.until(EC.visibility_of_element_located(self.CLOSE_PATIENT_DETAILS_TAB_LOCATOR))
        self.wait_and_click(self.CLOSE_PATIENT_DETAILS_TAB_LOCATOR)

    def click_add_encounter_button(self):
        self.wait_and_click(self.ADD_ENCOUNTER_BUTTON_LOCATOR)
        self.wait_for_spinner_to_disappear()
        time.sleep(5)
        #from Pages.CreateEncounterPage import CreateEncounterPage
        #return CreateEncounterPage(self.driver)

    def validate_encounter_created(self):
        today = datetime.now().strftime("%m/%d/%Y")   # e.g., "08/30/2025"
        elements = self.driver.find_elements(By.XPATH, f"//div[text()='{today}']")
    
        if not elements:
            raise AssertionError(f"No encounter found for {today}")
        else:
            print(f"✅ Encounter(s) found for {today}: {len(elements)}")

    def validate_and_download_encounter_pdf(self):
        today = datetime.now().strftime("%m/%d/%Y")   # e.g., "08/30/2025"
        elements = self.driver.find_elements(By.XPATH, f"//div[text()='{today}']")
    
        if not elements:
            raise AssertionError(f"No encounter found for {today}")
        else:
            print(f"✅ Encounter(s) found for {today}: {len(elements)}")

        elements[0].click()  # Click the first encounter found
        time.sleep(5)
        self.wait_for_spinner_to_disappear()
        self.wait_for_page_to_load()
        self.wait_and_click((By.XPATH, self.locator_reader.get("patient_details_page","download_pdf_button")))
        time.sleep(5)