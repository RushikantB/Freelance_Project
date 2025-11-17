from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Config.config import Config
import pytest
import os
from datetime import datetime
from Utils.ExcelTestSelector import ExcelTestSelector
from Utils.Device_Driver import get_android_driver, get_ios_driver
from Utils.ScreenshotUtil import ScreenshotUtil
from Utils.API_Helpers import APIClient
from Config.api_config import APIConfig

# ------- Fixture to initialize the WebDriver -------
# This fixture will be used in the test classes to initialize the WebDriver


@pytest.fixture(scope="class")
def driver_init(request):
    browser = Config.BROWSER.lower()
    print(f"\n👉 Browser from Config = {Config.BROWSER}\n")

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"Browser '{browser}' is not supported.")

    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()

# ------ Hook to take screenshot on test failure ------


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    screenshot_util = ScreenshotUtil(driver)
    test_name = item.name

    if report.when in ("setup", "call"):
        if report.failed:
            screenshot_util.take_screenshot(
                test_name, status="Fail", level="Final")
    elif report.passed:
        screenshot_util.take_screenshot(
            test_name, status="Pass", level="Final")


# ----Read test cases from Excel file and filter tests based on selection----
def pytest_collection_modifyitems(config, items):
    selector = ExcelTestSelector('Resources/TestCasesSelector.xlsx')
    selected_test_names = selector.get_selected_tests()

    selected_items = []
    deselected_items = []

    for item in items:
        # Get the test method or class name
        if any(test_name in item.nodeid for test_name in selected_test_names):
            selected_items.append(item)
        else:
            deselected_items.append(item)

    items[:] = selected_items
    config.hook.pytest_deselected(items=deselected_items)

# -------------------Device Driver Fixture-------------------
# This fixture will initialize the Appium driver for mobile testing based on the platform specified


@pytest.fixture(scope="function")
def mobile_driver(request):
    platform = request.config.getoption("--platform").lower()

    if platform == "android":
        driver = get_android_driver()
    elif platform == "ios":
        driver = get_ios_driver()
    else:
        raise ValueError("Invalid platform! Use 'android' or 'ios'.")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Choose platform: android or ios"
    )
# -----------------------------------------------------

# Optional: Token fixture (if you want to generate token once via login)


@pytest.fixture(scope="session")
def auth_token():
    # If token is empty, get it via login API
    if not APIConfig.AUTH_TOKEN:
        client = APIClient(use_auth=False)
        response = client.post("/api/login", data={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
        assert response.status_code == 200
        token = response.json()["token"]
        APIConfig.AUTH_TOKEN = token  # store it in config
    return APIConfig.AUTH_TOKEN

# -----------------------------------------------------------------------------
