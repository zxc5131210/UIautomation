"""Gesture Class."""
import time
from logger import Logger
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging
import os
from appium import webdriver

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
    def drag_drop_byelement(
        self,
        drag_element,
        drop_element,
        )-> None:
        self.touch_action.long_press(el=drag_element,duration=5000).move_to(drop_element).release().perform()
        self.logger.info('drag_drop complete.')
        pass
    def drag_drop_bylocate(
        self,
        drag_element,
        x,
        y
        )->None:
        self.touch_action.long_press(el=drag_element,duration=5000).move_to(x=x, y=y).release().perform()


    def double_tap(self, element) -> None:
        self.tap(element).tap(element).perform()
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
    
    def quit_driver(self):
        logging.info("Quit driver")
        self.driver.quit()
        pass

    def get_screenshot(self,filename)->None:
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        self.driver.save_screenshot(filename+"_%s.png" % nowTime)
        pass