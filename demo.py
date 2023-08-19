"""This is a demo test for gesture automation."""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import config
from gesture import Gesture

# Step 1 : Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = config.platformName
desired_caps['platformVersion'] = config.platformVersion
desired_caps['deviceName'] = config.deviceName
# desired_caps['appPackage'] = config.appPackage
# desired_caps['appActivity'] = config.appActivity
# desired_caps['udid'] = config.udid

# Step 2 : Create "Driver object"
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

#Step 3 : Create "gesture automation flow"
gesture = Gesture(driver=driver)

# drag and drop demo
drag_ele = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Chrome"]')
drop_ele = driver.find_element(AppiumBy.XPATH , '//android.widget.TextView[@content-desc="Chrome"]')
# gesture.drag_drop(drag_ele, drop_ele, x=0, y=-300)
gesture.tap(drag_ele)
time.sleep(3)
# gesture.double_tap(drag_ele)