"""This is a demo test for gesture automation."""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import config
from gesture import Gesture
from selenium.webdriver.common.by import By

# Step 1 : Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = config.platformName
desired_caps['platformVersion'] = config.platformVersion
desired_caps['deviceName'] = config.deviceName
desired_caps['udid'] = config.udid

# Step 2 : Create "Driver object"
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

#Step 3 : Create "gesture automation flow"
gesture = Gesture(driver=driver)

"""swipe to open the all apps view"""
start_x = 523
start_y = 1560
end_x = 481
end_y = 229
driver.swipe(start_x, start_y, end_x, end_y, duration=500)
place=(end_x,end_y)

# drag and drop demo
drag_ele = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Chrome"]')
drop_ele = driver.find_element(AppiumBy.XPATH , '//android.widget.TextView[@content-desc="Calendar"]')
gesture.drag_drop(drag_ele, drop_ele)
# gesture.tap(drag_ele)
time.sleep(3)
# gesture.double_tap(drag_ele)

"""verify the app is on the desktop or not"""
gesture.is_element_present(drag_ele)



