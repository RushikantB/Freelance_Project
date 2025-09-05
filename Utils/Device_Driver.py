from appium import webdriver
from Config.device_config import ANDROID_CAPS, IOS_CAPS, APPIUM_SERVER_URL

def get_android_driver():
    return webdriver.Remote(command_executor=APPIUM_SERVER_URL, desired_capabilities=ANDROID_CAPS)

def get_ios_driver():
    return webdriver.Remote(command_executor=APPIUM_SERVER_URL, desired_capabilities=IOS_CAPS)
