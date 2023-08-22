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
# event_gen = EventGen()
# event_gen.generate_event(json_path='./motion_flow.json', driver=driver)

#step1 : drag and drop
"""swipe to open the all apps view"""
gesture.swipe_up()

try:
    drag_ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Phone')
    gesture.drag_drop_bylocate(drag_ele,534,721)
    time.sleep(3)
    logger.debug(f'drag {drag_ele} on desktop success')

except :
    logger.debug(f'drag {drag_ele} is Fail')

'''verify App is on the desktop'''
try:
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Phone')
    logger.debug(f'{drag_ele} is on desktop')
except:
    logger.debug(f'{drag_ele} is not on desktop')

#step2 : move to second view
'''move the app form the first view to the second view'''
drag_ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Phone')
gesture.drag_drop_bylocate(drag_ele,1068,832)

'''verify the app is on second view or not'''
try:
    driver.find_element(AppiumBy.ID,'com.google.android.apps.nexuslauncher:id/date')
    logger.debug('This is desktop view')
    
    '''If it is homepage , change to second view'''
    gesture.swipe_left()

except:
    logger.debug('This is the second view')

#step3 :Tap the app on hot seat ,and check if app started
'''verify the app is on the hot seat'''
message_app = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Messages')



'''worst fuction to verify hot seat'''
# # 獲取元素的位置
# element_location = message_app.location
# element_y = element_location['y']
# print(element_y)

# # 獲取屏幕高度
# screen_size = driver.get_window_size()
# screen_height = screen_size['height']


# # 定義熱門應用欄的範圍（例如，底部10%的區域）
# hotseat_range = 0.3 * screen_height
# print(screen_height - hotseat_range)
# # 判斷元素的 Y 坐標是否在熱門應用欄的範圍內
# if element_y >= (screen_height - hotseat_range):
#     print("The element is in the Hot Seat.")
# else:
#     print("The element is not in the Hot Seat.")




driver.quit()
