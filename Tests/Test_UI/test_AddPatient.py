import time
import pytest
from Config.config import Config
from Pages import PatientDetailsPage
from Pages.LoginPage import LoginPage
from Pages.AddPatientPage import AddPatientPage
from Pages.PatientDetailsPage import PatientDetailsPage

@pytest.mark.usefixtures("driver_init")  # 👈 This connects your driver setup to the class
class TestAddPatient:

    def test_add_patient(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        add_patient_page = AddPatientPage(self.driver)
        add_patient_page.add_patient_selectfacility()
        first_expected, last_expected=add_patient_page.add_patient_demographics()
        add_patient_page.add_patient_address()
        add_patient_page.add_patient_payor()
        add_patient_page.add_patient_financial_responsible_party()

        patient_details_page = PatientDetailsPage(self.driver)
        first_actual, last_actual = patient_details_page.get_patient_name()
        actual_name = f"{first_actual} {last_actual}"

        #assert add_patient_page.verify_smoke_end_date_disabled(), "Smoke End Date field is enabled, but it should be disabled." 

        assert first_expected.lower() == first_actual, f"First name mismatch! Expected: {first_expected}, Got: {first_actual}"
        assert last_expected.lower() == last_actual, f"Last name mismatch! Expected: {last_expected}, Got: {last_actual}"

        print(f"✅ Patient name matched successfully: {first_actual} {last_actual}")

        expected_full_name = f"{first_expected} {last_expected}"

        # Compare ignoring case
        if actual_name.strip().lower() == expected_full_name.strip().lower():
            print("✅ Patient created successfully and validated patient names")
        else:
            raise AssertionError(
                f"❌ Patient name mismatch! Expected: {expected_full_name}, Got: {actual_name}"
        )

        time.sleep(5)
        
        patient_details_page.close_patient_details_tab()
        time.sleep(5)

        #assert first_expected == first_actual, \
        #f"Expected first name '{first_expected}', but got '{first_actual}'"
        #assert last_expected == last_actual, \
        #f"Expected last name '{last_expected}', but got '{last_actual}'"

        
        
    