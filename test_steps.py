from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import config
from gesture import Gesture
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

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

"""swipe to open the all apps view"""
start_x = 523
start_y = 1560
end_x = 481
end_y = 229
driver.swipe(start_x, start_y, end_x, end_y, duration=500)
place=(end_x,end_y)

"""add app-chrome to the desktop"""
chrome=driver.find_element(By.XPATH,'//android.widget.TextView[@content-desc="Chrome"]')
location=driver.find_element(By.XPATH,'	//android.widget.TextView[@content-desc="Calendar"]')
action = TouchAction(driver)

action.long_press(chrome,duration=5000).move_to(location).release().perform()
action.perform()

"""verify the app is on the desktop or not"""
try:
    driver.find_element(By.XPATH,'//android.widget.TextView[@content-desc="Chrome"]')
    print('pass')
except:
    print('fail')


# action.long_press(chrome,duration=5000)
# action.move_to(x=-1000,y=0)
# action.perform()


driver.quit()