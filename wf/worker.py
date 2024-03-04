import pyautogui
import pydirectinput
import autoit
from ahk import AHK


class Worker:
    def __init__(self):
        self.screenshot = None
        self.color = None
        self.width = 0
        self.height = 0
        self.test_counter = 100

    def worker(self):
        self.take_screenshot()
        self.color = self.find_color()
        if self.color is None:
            self.worker()
        x, y = self.color
        x = abs(x)
        y = abs(y)
        # pydirectinput.moveTo(x, y)
        # pydirectinput.leftClick()
        # autoit.mouse_move(x, y, 55550)
        # autoit.mouse_click("left")
        ahk = AHK()
        ahk.mouse_move(x, y, speed=4)
        ahk.click()
        # ahk.mouse_move(956, 1070, speed=500)
        self.test_counter -= 1
        self.color = None
        if self.test_counter > 0:
            self.worker()

    def take_screenshot(self):
        self.screenshot = pyautogui.screenshot()
        self.width, self.height = self.screenshot.size

    def find_color(self):
        color = [(61, 85, 186), (56, 79, 175), (59, 83, 184), (54, 77, 174)]

        for x in range(self.width):
            for y in range(self.height):
                if self.screenshot.getpixel((x, y)) in color:
                    return x, y
        return None



