"""Gesture Class."""
import time
from logger import Logger
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging

class Gesture:
    def __init__(self, driver) -> None:
        self.logger = Logger()
        if not driver:
            raise ValueError('driver can not be null.')
        self.driver = driver
        self.touch_action = TouchAction(self.driver)

        '''implicitly_wait setting'''
        self.wait = WebDriverWait(self.driver, 5)
        self.implicitly_wait_timeout = 15
        self.driver.implicitly_wait(self.implicitly_wait_timeout)      

    def tap(self, element) -> None:
        self.touch_action.tap(element).perform()
        self.logger.debug('tap complete.')
        pass
    def drag_drop(
        self,
        drag_element,
        drop_element,
        # x,
        # y 
        )-> None:
        # self.touch_action.long_press(el=drag_element, duration=5000).move_to(drop_element, x, y).release().perform()
        # self.touch_action.long_press(el=drag_element, duration=2000).perform()
        # time.sleep(2)
        # self.touch_action.move_to(el=drop_element, x=x, y=y).release().perform()
        self.touch_action.long_press(drag_element,duration=5000).move_to(drop_element).release().perform()
        self.logger.info('drag_drop complete.')
        pass
    def double_tap(self, element) -> None:
        self.touch_action.double_tap(element).perform()
        self.logger.debug('tap complete.')
        pass
    def keyboard(self) -> None:
        pass
    def back(self) -> None:
        pass
    def allapps_btn(self) -> None:
        pass
    def screenshot(self) -> None:
        pass
    def swipe(self) -> None:
        pass
    def double_finger(self) -> None:
        pass
    def longpress(self) -> None:
        pass

    def is_element_present(self,drag_elemnet)->None:
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(drag_elemnet)
            self.logger.info('The %d is present',drag_elemnet)
        except Exception:
            self.logger.info('The %d is not be found',drag_elemnet)
    def quit_driver(self):
        logging.info("Quit driver")
        self.driver.quit()
        pass

    def get_screenshot(self,filename)->None:
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        self.driver.get_screenshot_as_file(filename+"_%s.png" % nowTime)
        pass