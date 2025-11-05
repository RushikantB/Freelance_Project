import time
from Pages.BasePage import BasePage
from Utils.LocatorReader import LocatorReader
from selenium.webdriver.common.by import By
import os
import pyautogui


class RecruitmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator_reader = LocatorReader()

        self.ADDBUTTON_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_page", "add_button"))
        self.FNAME_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_add_candidate_page", "firstname"))
        self.MNAME_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_add_candidate_page", "middlename"))
        self.LNAME_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_add_candidate_page", "lastname"))
        self.VACANCYDROPDOWN_LOCATOR = (
            By.XPATH, self.locator_reader.get("recruitment_add_candidate_page", "select_vacancy"))
        self.SELECTQAROLE_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_add_candidate_page", "select_sr_qa_lead"))
        self.EMAIL_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_add_candidate_page", "email"))
        self.CONTACTNUMBER_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_add_candidate_page", "contactnumber"))
        self.UPLOADRESUME_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_add_candidate_page", "upload_resume"))
        self.SAVEBUTTON_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_add_candidate_page", "save_button"))
        self.CANCELBUTTON_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_add_candidate_page", "cancel_button"))
        self.VIEWCANDFNAME_LOCATOR = (
            By.XPATH, self.locator_reader.get("recruitment_candidate_page", "view_fName"))
        self.VIEWCANDLNAME_LOCATOR = (
            By.XPATH, self.locator_reader.get("recruitment_candidate_page", "view_lName"))
        self.SHORTLIST_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_candidate_page", "shorlist_button"))
        self.REJECT_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_candidate_page", "reject_button"))
        self.EDITLABEL_LOCATOR = (By.XPATH, self.locator_reader.get(
            "recruitment_candidate_page", "edit_label"))

    def add_candidiate(self):
        fName, mName, lName = self.generate_names()
        file_path = os.path.abspath(
            "Users/rushikantbhosale/Documents/Rushikant/Automation/Freelance_Framework/Resources/Test.docx")
        self.wait_and_click(self.ADDBUTTON_LOCATOR)
        self.enter_text(self.FNAME_LOCATOR, fName)
        self.enter_text(self.MNAME_LOCATOR, mName)
        self.enter_text(self.LNAME_LOCATOR, lName)
        self.wait_and_click(self.VACANCYDROPDOWN_LOCATOR)
        time.sleep(2)
        self.wait_and_click(self.SELECTQAROLE_LOCATOR)
        time.sleep(3)
        self.enter_text(self.EMAIL_LOCATOR, "test@test.com")
        self.enter_text(self.CONTACTNUMBER_LOCATOR, "9445435345")
        time.sleep(4)
        """
        upload_button = self.driver.find_element(
            By.XPATH, "//div[text()='Browse']")
        upload_button.click()
        time.sleep(3)
        pyautogui.write(file_path)
        time.sleep(3)
        pyautogui.press("enter")
        time.sleep(3)
        """
        self.wait_and_click(self.SAVEBUTTON_LOCATOR)
        self.wait_for_spinner_to_disappear()
        self.wait_for_page_to_load()
        time.sleep(4)

        fullname = fName+mName+lName
        print(fullname)

        self.wait_and_click(self.EDITLABEL_LOCATOR)
        time.sleep(2)

        get_fName = self.driver.find_element(
            *self.VIEWCANDFNAME_LOCATOR).get_attribute("value")
        get_lName = self.driver.find_element(
            *self.VIEWCANDLNAME_LOCATOR).get_attribute("values")

        print(get_fName)
        print(get_fName)

        '''
        if fName != get_fName and lName == get_lName:
            print("First name does not match")
        elif fName == get_fName and lName != get_lName:
            print("Last name does not match")
        else:
            print(f"Candidate created successfully: {get_fName} {get_lName}")
        '''
        '''
        assert (fName or "").casefold(
        ) == (get_fName or "").casefold(), "First name does not match"
        
        assert (lName or "").casefold() == (get_lName or "").casefold(), "Last name does not match"
        print(f"Candidate created successfully: {get_fName} {get_lName}")
        '''

        assert (fName or "").lower() == (
            get_fName or "").lower(), "First name does not match"
        # assert (lName or "").lower() == (
        #    get_lName or "").lower(), "Last name does not match"
        print(f"Candidate created successfully: {get_fName} {get_lName}")
