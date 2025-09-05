import os
from datetime import datetime


class ScreenshotUtil:
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, test_name, status="Pass", level="Final"):
        """
        level = "Steps" or "Final"
        status = "Pass" or "Fail"
        """
        time_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        #screenshot_folder = os.path.join("Screenshots", test_name, level, status)
        screenshot_folder = os.path.join("Screenshots", status, level, test_name)
        os.makedirs(screenshot_folder, exist_ok=True)

        screenshot_name = f"{level}_{status}_{time_stamp}.png"
        path = os.path.join(screenshot_folder, screenshot_name)
        self.driver.save_screenshot(path)
        print(f"Screenshot saved to {path}")
