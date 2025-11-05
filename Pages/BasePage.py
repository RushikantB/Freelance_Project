import random
import string
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os
from datetime import datetime
from Utils.ScreenshotUtil import ScreenshotUtil
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
        self.reader = None  # Placeholder for ExcelReader instance
        self.screenshot_util = ScreenshotUtil(self.driver)

        self.generated_numbers = set()         # <-- needed for generate_unique_number()
        self.generated_mrns = set()            # <-- needed for generate_mrn()
        self.generated_mbis = set()            # <-- needed for generate_mbi()
        self.generated_medicaid_numbers = set()
        self.allowed_digits = list("0123456789")
        self.allowed_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def set_excel_reader(self, reader):
        """Set the ExcelReader instance for this page"""
        self.reader = reader

    # -------- Wait for an element to be clickable and click it, with optional screenshot --------
    def wait_and_click(self, locator, test_name=None):
        try:
            wait = WebDriverWait(self.driver, 20)
            element = wait.until(EC.visibility_of_element_located(locator))
            element.click()

            if test_name:
                self.screenshot_util.take_screenshot(
                    test_name, status="Pass", level="Steps")

        except Exception as e:
            print(f"Error in wait_and_type: {e}")
            if test_name:
                self.screenshot_util.take_screenshot(
                    test_name, status="Fail", level="Steps")
            raise

    def get_text(self, locator, test_name=None):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator))
            text = element.text.strip()
            if test_name:
                self.screenshot_util.take_screenshot(
                    test_name, status="Pass", level="Steps")
            return text
        except Exception as e:
            print(f"Error in get_text: {e}")
            if test_name:
                self.screenshot_util.take_screenshot(
                    test_name, status="Fail", level="Steps")
            raise

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        # self.screenshot_util.take_screenshot("enter_text", status="Pass")

    def select_by_visible_text(self, locator, text):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(text)

    def select_by_value(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(value)

    def select_by_index(self, locator, index):
        select = Select(self.driver.find_element(*locator))
        select.select_by_index(index)

    def wait_for_page_to_load(self, locator=None, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script(
                    'return document.readyState') == 'complete'
            )
            if locator:
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
            print("Page fully loaded.")
            return True
        except Exception as e:
            print(f"Page load failed: {e}")
            return False

    # Wait for an element to be visible
    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be visible and return it"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise Exception(f"Element not visible after {timeout}s: {locator}")

    # Select an option from a dropdown or suggestion list
    def select_from_suggestions(self, suggestion_locator, match_text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        suggestions = wait.until(
            EC.presence_of_all_elements_located(suggestion_locator))

        for suggestion in suggestions:
            if match_text.lower() in suggestion.text.lower():
                suggestion.click()
                return
        raise Exception(f"No matching suggestion found for: {match_text}")

    # Generate unique names (<=10 chars) using timestamp + random char
    def generate_names(self):
        """Generate unique names (<=10 chars) using timestamp + random char"""
        ts_suffix = str(int(time.time() * 1000))[-3:]
        rand_char1 = random.choice(string.ascii_uppercase)
        rand_char2 = random.choice(string.ascii_lowercase)

        first_name = "FN" + rand_char1 + ts_suffix
        middle_name = "MN" + ts_suffix
        last_name = "LN" + rand_char2 + ts_suffix

        return first_name[:10], middle_name[:10], last_name[:10]

    def generate_mrn(self):
        """Generate a unique MRN (<=10 chars) using timestamp + random digits"""
        # Take last 6 digits of current timestamp (seconds)
        timestamp_part = str(int(time.time()))[-6:]
        # Add a 2-digit random number for extra uniqueness
        random_part = str(random.randint(10, 99))
        # Final MRN (ensures max 10 characters)
        mrn = f"MRN{timestamp_part[:5]}{random_part}"
        return mrn

    def generate_unique_number(self):
        while True:
            # Generate a random 9-digit number (100000000 to 999999999)
            number = random.randint(100000000, 999999999)
            if number not in self.generated_numbers:
                self.generated_numbers.add(number)
                return number

    def generate_mbi(self):
        # Generate a realistic MBI (11 characters, alternating letters and digits)
        mbi = []
        for i in range(11):
            if i % 2 == 0:  # alternate digits and letters for realism
                mbi.append(random.choice(self.allowed_digits))
            else:
                mbi.append(random.choice(self.allowed_letters))
        return "".join(mbi)

    def generate_medicaid_number(state=None):
        # Generate a Medicaid number based on state rules"""
        if state == "CA":  # California - 14 digit numeric
            return ''.join(random.choices(string.digits, k=14))

        elif state == "TX":  # Texas - 9 digit numeric
            return ''.join(random.choices(string.digits, k=9))

        elif state == "NY":  # New York - 8 character alphanumeric
            return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        else:
            # Generic Medicaid ID (random length between 9 and 14 digits)
            length = random.randint(9, 14)
            return ''.join(random.choices(string.digits, k=length))

    def is_element_disabled_or_readonly(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        disabled = element.get_attribute("disabled")
        readonly = element.get_attribute("readonly")
        return (disabled is not None) or (readonly is not None)

    def wait_for_spinner_to_disappear(self, spinner_locator=(By.CSS_SELECTOR, ".spinner"), timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(spinner_locator)
            )
            print("✅ Spinner disappeared.")
        except TimeoutException:
            print("⚠️ Spinner still visible after timeout.")
