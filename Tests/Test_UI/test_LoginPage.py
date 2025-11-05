import pytest
from Pages.LoginPage import LoginPage
from Config.config import Config


# 👈 This connects your driver setup to the class
@pytest.mark.usefixtures("driver_init")
class TestLoginPage:

    def test_login_valid_user(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        # home_page = HomePage_Dashboard(self.driver)
        # assert home_page.verify_home_page_loaded(), "Home page did not load successfully after login."
