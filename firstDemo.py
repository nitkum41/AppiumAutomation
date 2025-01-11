from appium import webdriver
from typing import Any, Dict

from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UIAutomator2",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "language": "en",
    "locale": "US"
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))

element = driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Battery"]')

element.click()

driver.quit()
