"""This is a demo test for gesture automation."""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import config
from gesture import Gesture
from selenium.webdriver.common.by import By
from logger import Logger
from event_generator import EventGen

logger=Logger()

# Step 1 : Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = config.platformName
desired_caps['platformVersion'] = config.platformVersion
desired_caps['deviceName'] = config.deviceName
desired_caps['udid'] = config.udid

# Step 2 : Create "Driver object"
driver = webdriver.Remote(f'http://{config.host}:{config.port}/wd/hub', desired_caps)

#Step 3 : Create "gesture automation flow"
gesture = Gesture(driver=driver)
event_gen = EventGen()
event_gen.generate_event(json_path='./motion_flow.json', driver=driver)

"""swipe to open the all apps view"""
gesture.swipe_up()

# drag and drop demo
try:
    drag_ele = driver.find_element(AppiumBy.XPATH,'	//android.widget.TextView[@content-desc="Phone"]')
    drop_ele = driver.find_element(AppiumBy.XPATH , '//android.widget.TextView[@content-desc="Calendar"]')
    gesture.drag_drop_byelement(drag_ele, drop_ele)
    time.sleep(3)
    logger.debug(f'drag {drag_ele} on desktop success')

except :
    logger.debug(f'drag {drag_ele} is Fail')

'''verify App is on the desktop'''
try:
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Phone"]')
    logger.debug(f'{drag_ele} is on desktop')
except:
    logger.debug(f'{drag_ele} is not on desktop')

'''move the app form the first view to the second view'''
drag_ele = driver.find_element(AppiumBy.XPATH,'	//android.widget.TextView[@content-desc="Phone"]')
gesture.drag_drop_bylocate(drag_ele,1068,832)

'''verify the app is on second view or not'''
try:
    driver.find_element(AppiumBy.ID,'com.google.android.apps.nexuslauncher:id/date')
    logger.debug('This is desktop view')
    
    '''If it is homepage , change to second view'''
    gesture.swipe_left()

except:
    logger.debug('This is the second view')