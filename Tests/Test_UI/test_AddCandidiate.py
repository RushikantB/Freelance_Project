import pytest

from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage
from Pages.RecruitmentPage import RecruitmentPage


@pytest.mark.usefixtures("driver_init")
class TestAddCandidiate:

    def test_add_candidiate(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_on_recruitment_link()
        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.add_candidiate()
