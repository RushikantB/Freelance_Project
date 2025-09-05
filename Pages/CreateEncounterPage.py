import time
from Pages.BasePage import BasePage
from Utils.Excel_Reader import ExcelReader
from Utils.LocatorReader import LocatorReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class CreateEncounterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator_reader = LocatorReader()
        self.reader = ExcelReader()

        self.SELECT_VISIT_TYPE_BUTTON = (By.XPATH, self.locator_reader.get("create_encounter_page", "select_visit_type"))
        self.CREATE_ENCOUNTER_BUTTON = (By.XPATH, self.locator_reader.get("create_encounter_page", "create_encounter_button"))
        self.ENCOUNTER_EXISTS_POPUP = (By.XPATH, self.locator_reader.get("create_encounter_page", "encounter_exists_popup"))
        self.CONTINUE_BUTTON = (By.XPATH, self.locator_reader.get("create_encounter_page", "continue_button"))
        
        self.HISTORY_ENTERROOM_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "history_enter_room"))
        self.HISTORY_MEDICATION_LIST_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "history_medication_list"))
        self.HISTORY_ALLERGY_LIST_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "history_enter_allergy_list"))    
        self.VITALS_HIGHT_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "vitals_hight"))
        self.VITALS_WEIGHT_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "vitlas_weight"))
        self.VITALS_BMI_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "vitals_bmi"))
        self.VITALS_TEMPERATURE_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "vitals_temperature"))
        self.VITALS_PULSE_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "vitals_pulse"))
        self.VITALS_PAINLEVEL_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "vitals_painlevel"))
        self.PHYSICAL_EXAM_ENMT = (By.XPATH, self.locator_reader.get("create_encounter_page", "physical_exam_enter_enmt"))
        self.LABS_ENTER_LAB_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "labs_enter_labs"))
        self.ASSESSMENTANDPLAN_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "assessment_and_plan_enter_anp"))

        self.PROBLEM_LIST_TAB = (By.XPATH, self.locator_reader.get("create_encounter_page", "problem_list_tab"))
        self.ICD_TEXTBOX = (By.XPATH, self.locator_reader.get("create_encounter_page", "icd_textbox"))
        self.CPT_TEXTBOX = (By.XPATH, self.locator_reader.get("create_encounter_page", "cpt_textbox"))
        self.ADD_ICD_PLUS_BUTTON = (By.XPATH, self.locator_reader.get("create_encounter_page", "add_icd_plus_button"))
        self.ADD_CPT_PLUS_BUTTON = (By.XPATH, self.locator_reader.get("create_encounter_page", "add_cpt_plus_button"))
        
        self.ATTACH_ASSESSMENT_BUTTON_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "attach_assessment"))
        self.ADD_NEW_ATTACHMENT_BUTTON_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "add_new_attach_assessment"))
        self.SELECT_ASSESSMENT_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "select_assessment"))
        self.CONTINIUE_ADD_ASSESSMENT_BUTTON_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "continue_button_add_assessment"))
        self.CLICK_ALL_QUESTIONS_BUTTON_ASSESSMENT = (By.XPATH, self.locator_reader.get("create_encounter_page", "click_all_questions_button"))
        self.CANCEL_ASSESSMET_BUTTON_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "cancel_button_add_assessment"))   
        self.SAVE_ADD_ASSESSMENT_BUTTON_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "save_button_add_assessment"))
        self.SIGN_AND_CLOSE_BUTTON_ADD_ASSESSMENT_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "sign_and_close_button_add_assessment"))    
        self.ATTACH_BUTTON_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "attach_button"))
        self.CANCEL_BUTTON_LOCATOR = (By.XPATH, self.locator_reader.get("create_encounter_page", "cancel_button"))
        self.COUNT_0_ATTACHMENT = (By.XPATH, self.locator_reader.get("create_encounter_page", "0_attachment_count"))
        self.COUNT_1_ATTACHMENT = (By.XPATH, self.locator_reader.get("create_encounter_page", "1_attachment_count"))


        self.SIGN_AND_CLOSE_BUTTON = (By.XPATH, self.locator_reader.get("create_encounter_page", "sign_and_close_button"))   

    def create_encounter(self):
        self.set_excel_reader(self.reader)
        self.reader.select_sheet(sheet_name="CreateEncounterPage")
        data=self.reader.get_row_as_dict(2)
        visit_type=data['Select_Visit_Type']
        self.select_by_value(self.SELECT_VISIT_TYPE_BUTTON, visit_type)
        time.sleep(5)
        self.wait_and_click(self.CREATE_ENCOUNTER_BUTTON)
        try:
            self.wait.until(EC.visibility_of_element_located(self.ENCOUNTER_EXISTS_POPUP))
            print("Encounter exists popup appeared")
            self.wait_and_click(self.CONTINUE_BUTTON)
            time.sleep(5)
        except:
            print("No encounter exists popup, proceeding")  

    def enter_medical_details(self):
        self.enter_text(self.HISTORY_ENTERROOM_LOCATOR, "A-101")
        self.enter_text(self.HISTORY_MEDICATION_LIST_LOCATOR, "Medications reviewed and reconciled")
        self.enter_text(self.HISTORY_ALLERGY_LIST_LOCATOR, "No Known Drug Allergies ")
        self.enter_text(self.VITALS_HIGHT_LOCATOR, "5.7")
        self.enter_text(self.VITALS_WEIGHT_LOCATOR, "70")
        self.enter_text(self.VITALS_BMI_LOCATOR, "24")
        self.enter_text(self.VITALS_TEMPERATURE_LOCATOR, "98.6")
        self.enter_text(self.VITALS_PULSE_LOCATOR, "80")
        self.enter_text(self.VITALS_PAINLEVEL_LOCATOR, "2")
        self.enter_text(self.PHYSICAL_EXAM_ENMT, "Physical exam normal")
        self.enter_text(self.LABS_ENTER_LAB_LOCATOR, "Labs reviewed during visit")
        self.enter_text(self.ASSESSMENTANDPLAN_LOCATOR, "Assessment and plan entered")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)

    def click_on_problem_list_tab(self):        
        self.wait_and_click(self.PROBLEM_LIST_TAB)

    def enter_select_icd_code(self):
        self.set_excel_reader(self.reader)
        self.reader.select_sheet(sheet_name="CreateEncounterPage")
        data=self.reader.get_row_as_dict(2)
        icd_code=data['ICD_Code']
        self.enter_text(self.ICD_TEXTBOX, icd_code + Keys.ENTER)
        time.sleep(4)
        self.wait_and_click(self.ADD_ICD_PLUS_BUTTON)

    def enter_select_cpt_code(self):
        self.set_excel_reader(self.reader)
        self.reader.select_sheet(sheet_name="CreateEncounterPage")
        data=self.reader.get_row_as_dict(2)
        cpt_code=data['CPT_Code']
        self.enter_text(self.CPT_TEXTBOX, cpt_code + Keys.ENTER)
        time.sleep(4)
        self.wait_and_click(self.ADD_CPT_PLUS_BUTTON)
        time.sleep(5)

    def add_attachments(self):
        self.wait_and_click(self.ATTACH_ASSESSMENT_BUTTON_LOCATOR)
        time.sleep(3)
        self.wait_and_click(self.ADD_NEW_ATTACHMENT_BUTTON_LOCATOR)
        time.sleep(3)

        self.set_excel_reader(self.reader)
        self.reader.select_sheet(sheet_name="CreateEncounterPage")
        data=self.reader.get_row_as_dict(2)
        assessment=data['Select_Assessment']
        self.select_by_value(self.SELECT_ASSESSMENT_LOCATOR, assessment)    
        self.wait_and_click(self.CONTINIUE_ADD_ASSESSMENT_BUTTON_LOCATOR)
        time.sleep(3)
        self.wait_and_click(self.CLICK_ALL_QUESTIONS_BUTTON_ASSESSMENT)
        time.sleep(3)
        self.wait_and_click(self.SIGN_AND_CLOSE_BUTTON_ADD_ASSESSMENT_LOCATOR)
        time.sleep(3)
        self.wait_for_spinner_to_disappear()
        self.wait_for_page_to_load()
        attch_button_text = self.get_text(self.ATTACH_BUTTON_LOCATOR)
        #expected_text = "Attachment"
        #assert expected_text in attch_button_text, f"Expected '{expected_text}' in button text, but got '{attch_button_text}'"
        print(f"Attachment button text after adding assessment: {attch_button_text}")
        self.wait_and_click(self.ATTACH_BUTTON_LOCATOR)
        time.sleep(3)
        self.wait_for_spinner_to_disappear()
        self.wait_for_page_to_load()

    def validate_attachment_added(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.COUNT_1_ATTACHMENT))
            print("Attachment added successfully.")
            return True
        except Exception as e:
            print(f"Attachment not added: {e}")
            return False    
        
    def click_on_sign_and_close_button(self):
        #SIGN_AND_CLOSE_BUTTON = (By.XPATH, self.locator_reader.get("create_encounter_page", "sign_and_close_button"))
        self.wait_and_click(self.SIGN_AND_CLOSE_BUTTON)
        time.sleep(10)
        self.wait_for_spinner_to_disappear()
        self.wait_for_page_to_load()

    def create_encounter_for_matrix_patient(self):
        self.set_excel_reader(self.reader)
        self.reader.select_sheet(sheet_name="CreateEncounterPage")
        data=self.reader.get_row_as_dict(2)
        visit_type=data['Select_Visit_Type']
        self.select_by_value(self.SELECT_VISIT_TYPE_BUTTON, visit_type)
        time.sleep(5)
        self.wait_and_click(self.CREATE_ENCOUNTER_BUTTON)
        try:
            self.wait.until(EC.visibility_of_element_located(self.ENCOUNTER_EXISTS_POPUP))
            print("Encounter exists popup appeared")
            self.wait_and_click(self.CONTINUE_BUTTON)
            time.sleep(5)
        except:
            print("No encounter exists popup, proceeding")
            
        self.wait_and_click(self.PROBLEM_LIST_TAB)    
