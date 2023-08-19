"""Gesture Class."""
import time
from logger import Logger
from appium.webdriver.common.touch_action import TouchAction


class Gesture:
    def __init__(self, driver) -> None:
        self.logger = Logger()
        if not driver:
            raise ValueError('driver can not be null.')
        self.driver = driver
        self.touch_action = TouchAction(self.driver)
    def tap(self, element) -> None:
        self.touch_action.tap(element).perform()
        self.logger.debug('tap complete.')
        pass
    def drag_drop(
        self,
        drag_element,
        drop_element,
        x,
        y) -> None:
        self.touch_action.long_press(el=drag_element, duration=3000).move_to(drop_element, x, y).release().perform()
        self.logger.debug('drag_drop complete.')
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
