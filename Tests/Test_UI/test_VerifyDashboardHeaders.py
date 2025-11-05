import pytest

from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("driver_init")
class TestDashboardHeaders:

    def test_dashboard_header(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.verify_dashboard_headers()
        dashboard_page.click_on_admin_link()
