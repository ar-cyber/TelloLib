import djitellopy
from djitellopy import Tello
import sys

import cv2
import uuid
# import keyboard

class TelloLib(Tello):
    def __init__(self, host: str="192.168.10.1", port: int=8889, retry_count: int=50) -> Tello:
        super().__init__(host, port, retry_count)
    def CheckBatteryLevel(self) -> None:
        '''
        Background process to check if the battery is too low (or if the land button is pressed). Returns `None`
        '''
        while True:
            try:
                if self.get_battery() <= 5:
                    self.emergency()
                    input("BATTERY IS TOO LOW. THE DRONE HAS BEEN PREMATURELY STOPPED. PLEASE PRESS ENTER TO END THE PROGRAM.")
                    sys.exit()
                else:
                    pass
            except:
                raise NotImplementedError("Battery check is not possible on your device.")
                
    def square(self, length: int=20) -> bool:
        '''
        Creates a square with each side being the length parameter.
        '''
        try:
            for x in range(5):
                self.move_forward(length)
                self.rotate_clockwise(90)
            return True
        except:
            return False
    def circle(self, rad: int=10) -> bool:
        '''
        Creates a circle with the radius specified above.
        '''
        try:
            self.move_forward(rad)
            for x in range(361):
                self.move_forward(5)
                self.rotate_clockwise(1)
            return True
        except: return False
    def polygon(self,sides: int, angle: int, size: int=5) -> bool:
        '''Creates a regular polygon with the parameters sides, angle, and size'''
        try:
            self.move_forward(size)
            for x in range(sides):
                self.move_forward(size)
                self.rotate_clockwise(angle)
            return True
        except:
            return False
    def irregularpolygon(self,sides: int, sidesizes: list, angles: list, take_picture: bool = False) -> bool | None:
        '''Creates an irregular polygon. `sidesizes` and `angles` are list objects.'''
        previous = angles[0]
        try:
            for x in range(sides):
                angle = angles[x]
                
                sidesize = sidesizes[x]
                if previous != angle: self.rotate_clockwise(previous)
                self.rotate_counter_clockwise(angle) # Do this because the angles go in counter clockwise rotations.

                self.move_forward(sidesize)
                if take_picture:
                    cv2.imwrite(f"{uuid.uuid4()}.png", self.get_frame_read().frame)
                previous = angle
            return True
        except:
            return False
