import pytest

@pytest.mark.usefixtures()
class TestCheckLogic:

    def test_check_logic(self):
        # Example test logic
        self.driver.get("https://uat.pacehr.thesnfist.com/login")
