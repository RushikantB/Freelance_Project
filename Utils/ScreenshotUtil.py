import os
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver


class ScreenshotUtil:
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, test_name, status="Pass", level="Final"):
        """
        level = "Steps" or "Final"
        status = "Pass" or "Fail"
        """
        time_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # screenshot_folder = os.path.join("Screenshots", test_name, level, status)
        screenshot_folder = os.path.join(
            "Screenshots", status, level, test_name)
        os.makedirs(screenshot_folder, exist_ok=True)

        screenshot_name = f"{level}_{status}_{time_stamp}.png"
        path = os.path.join(screenshot_folder, screenshot_name)
        self.driver.save_screenshot(path)
        print(f"Screenshot saved to {path}")


class ScreenshotUtil_Manual:
    def __init__(self, base_dir="Screenshots/ManualScreenshots"):
        self.base_dir = base_dir
        self.session_folder = None

    def create_session_folder(self):
        """Create a timestamp folder for each test suite run."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.session_folder = os.path.join(self.base_dir, timestamp)
        os.makedirs(self.session_folder, exist_ok=True)

    def manual_shot(self, driver: WebDriver, test_name: str, status: str = "Pass"):
        """
        Capture screenshot for given test and status (Pass/Fail).

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            test_name (str): Name of the test case.
            status (str): 'Pass' or 'Fail'
        """
        if not self.session_folder:
            self.create_session_folder()

        # Create subfolders for test and status
        test_folder = os.path.join(self.session_folder, test_name)
        status_folder = os.path.join(test_folder, status.capitalize())
        os.makedirs(status_folder, exist_ok=True)

        # Screenshot file path
        file_name = f"{test_name}_{datetime.now().strftime('%H-%M-%S')}.png"
        file_path = os.path.join(status_folder, file_name)

        try:
            driver.save_screenshot(file_path)
            print(f"✅ Screenshot saved at: {file_path}")
            return file_path
        except Exception as e:
            print(f"❌ Error taking screenshot: {e}")
            return None

    def manual_screenshot():
        file_name = ""
