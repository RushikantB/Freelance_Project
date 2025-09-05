import pytest
from Pages.CreateEncounterPage import CreateEncounterPage
from Pages.PatientDetailsPage import PatientDetailsPage
from Pages.PatientsPage import PatientsPage
from Pages.HomePage_Dashboard import HomePage_Dashboard
from Pages.LoginPage import LoginPage

@pytest.mark.usefixtures("driver_init")  # 👈 This connects your driver setup to the class
class TestCreateEncounter:

    def test_create_encounter(self):
        login_page = LoginPage(self.driver)
        login_page.login()
      
        dashboard_page=HomePage_Dashboard(self.driver)
        dashboard_page.navigate_patients_tab()

        patients_page=PatientsPage(self.driver)
        patients_page.search_patient_and_navigate_to_patientdetails_page()


        patient_details_page=PatientDetailsPage(self.driver)
        patient_name=patient_details_page.get_patient_name()
        print(f"Patient Name: {patient_name[0]} {patient_name[1]}")
        
        create_encounter_page=CreateEncounterPage(self.driver)
        
        patient_details_page.click_add_encounter_button()

        #----------------------------------------------------     
        create_encounter_page.create_encounter()
        create_encounter_page.enter_medical_details()
        create_encounter_page.click_on_problem_list_tab()
        create_encounter_page.enter_select_icd_code()
        create_encounter_page.enter_select_cpt_code()
        create_encounter_page.add_attachments()
        assert create_encounter_page.validate_attachment_added(), "Attachment was not added successfully."
        create_encounter_page.click_on_sign_and_close_button()
        #----------------------------------------------------
        patient_details_page.validate_encounter_created()
        patient_details_page.validate_and_download_encounter_pdf()
        patient_details_page.close_patient_details_tab()
        
        print("✅ Encounter created successfully.")
        
        