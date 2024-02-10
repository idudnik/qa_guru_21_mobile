import os
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser
from dotenv import load_dotenv

load_dotenv()
login = os.environ.get('USER_NAME')
access_key = os.environ.get('ACCESS_KEY')


@pytest.fixture(scope='function', autouse=True)
def android_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": login,
            "accessKey": access_key
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield
    browser.quit()