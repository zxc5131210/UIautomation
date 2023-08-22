"""Event generator.
Event generator will read a .json file and generate event.
"""

from logger import Logger
import json
from gesture import Gesture
from appium.webdriver.common.appiumby import AppiumBy


class EventGen:
    def __init__(self) -> None:
        self.logger = Logger()
    def read_json(self, json_path: str) -> dict:
        with open(json_path, encoding='utf-8') as fp:
            flow = json.load(fp)
            return flow
    def generate_event(self, json_path: str, driver):
        """Read a json file and generate events."""
        evnet_flow = self. read_json(json_path)
        flow = evnet_flow['step']
        print(flow)
        gesture = Gesture(driver)
        for event in flow:
            seq = event['squence']
            ele = event['element']
            ges = event['gesture']
            # perform gesture
            if ges == 'tap':
                element = driver.find_element(
                    AppiumBy.XPATH ,
                    ele
                )
                gesture.tap(element)
            elif ges == 'screenshot':
                filename = event['args'][-1]
                gesture.screenshot(save_location=f'./{filename}')
            else:
                self.logger.warring(f'gesture type: {ges} not define.')
                continue
            self.logger.debug(f'Sequence {seq} {ges} complete.')


if __name__  == '__main__':
    eventgen = EventGen()
    # eventgen.generate_event('./motion_flow.json')
    