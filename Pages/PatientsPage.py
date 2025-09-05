import time
from Pages.BasePage import BasePage
from Utils.Excel_Reader import ExcelReader
from Utils.LocatorReader import LocatorReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PatientsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator_reader = LocatorReader()
        self.reader = ExcelReader()

        self.PATIENT_NAME_HEADER_LOCATOR = (By.XPATH, self.locator_reader.get("patients_page","patient_name_header"))
        self.SEARCH_PATIENT_TEXTBOX = (By.XPATH, self.locator_reader.get("patients_page","search_patient_textbox"))
        self.SELECT_PATIENT_FROM_SUGGESTION = (By.XPATH, self.locator_reader.get("patients_page","select_patient_from_suggestion"))


    def verify_patient_page_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PATIENT_NAME_HEADER_LOCATOR))
            patientpage_tab_text=self.get_text(self.PATIENT_NAME_HEADER_LOCATOR)
            print(f"Home page loaded successfully: {patientpage_tab_text}")
            return True
        except Exception as e:
            print(f"Home page did not load: {e}")
            return False

    def search_patient_and_navigate_to_patientdetails_page(self):
        self.set_excel_reader(self.reader)
        self.reader.select_sheet(sheet_name="CommonData")
        data=self.reader.get_row_as_dict(2)
        patient_name=data['PatientName']
        self.enter_text(self.SEARCH_PATIENT_TEXTBOX, patient_name)
        time.sleep(5)        
        self.select_from_suggestions(self.SELECT_PATIENT_FROM_SUGGESTION, patient_name)
        time.sleep(5)  # Wait for the page to load
        
    def search_matrixcarepatient_and_navigate_to_patientdetails_page(self):
        self.set_excel_reader(self.reader)
        self.reader.select_sheet(sheet_name="CommonData")
        data=self.reader.get_row_as_dict(3)
        patient_name=data['PatientName']
        self.enter_text(self.SEARCH_PATIENT_TEXTBOX, patient_name)
        time.sleep(5)        
        self.select_from_suggestions(self.SELECT_PATIENT_FROM_SUGGESTION, patient_name)
        time.sleep(5)  # Wait for the page to load    

    def search_pointclickcarepatient_and_navigate_to_patientdetails_page(self):
        self.set_excel_reader(self.reader)
        self.reader.select_sheet(sheet_name="CommonData")
        data=self.reader.get_row_as_dict(4)
        patient_name=data['PatientName']
        self.enter_text(self.SEARCH_PATIENT_TEXTBOX, patient_name)
        time.sleep(5)        
        self.select_from_suggestions(self.SELECT_PATIENT_FROM_SUGGESTION, patient_name)
        time.sleep(5)  # Wait for the page to load    