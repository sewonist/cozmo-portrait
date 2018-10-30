from animation import Animation
from time import sleep
from cozmo.util import degrees, radians, distance_mm, speed_mmps, Pose, Angle

class Circle(Animation):
    def Draw(self):
        sleep(7)
        self.Ready()
        sleep(0.5)
        self.LiftUp()
        sleep(1)
        self.LiftDown()
        sleep(0.1)

        for _ in range(6):
            self.cozmo.turn_in_place(degrees(360), speed=Angle(1)).wait_for_completed()

        self.LiftUp()