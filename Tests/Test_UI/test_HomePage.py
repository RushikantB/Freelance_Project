import pytest
from Pages.LoginPage import LoginPage   
from Pages.HomePage_Dashboard import HomePage_Dashboard
from Config.config import Config

@pytest.mark.usefixtures("driver_init")  # 👈 This connects your driver setup to the class
class TestHomePage:
    def test_home_page_loaded(self):
        login_page = LoginPage(self.driver)
        login_page.login()

        home_page = HomePage_Dashboard(self.driver)
        assert home_page.verify_home_page_loaded(), "Home page did not load successfully."
