import cozmo
from time import sleep
from flower import Flower
from cube import Cube
from circle import Circle

class Portrait:
    def __init__(self, robot: cozmo.robot.Robot):
        self.cozmo = robot
        self.lift_up = 0
        self.lift_down = 0
        self.head_up = 0
        self.head_down = 0
        self.go_fast = 0
        self.go_slow = 1
        self.animations = [Cube(self.cozmo),
                           Circle(self.cozmo),
                           Flower(self.cozmo)]

    def Draw(self, i: int):
        self.animations[i].Draw()

    def LiftUp(self):
        self.lift_up = 1
        self.lift_down = 0
        self.update_lift()
        sleep(0.1)
        self.lift_up = 0
        self.update_lift()

    def LiftDown(self):
        self.lift_up = 0
        self.lift_down = 1
        self.update_lift()
        sleep(0.1)
        self.lift_down = 0
        self.update_lift()

    def Ready(self):
        self.lift_up = 0
        self.lift_down = 1
        self.update_lift()

    def Reset(self):
        self.lift_up = 1
        self.lift_down = 0
        self.update_lift()

    def update_lift(self):
        lift_speed = self.pick_speed(8, 3, 1)
        lift_vel = (self.lift_up - self.lift_down) * lift_speed
        self.cozmo.move_lift(lift_vel)

    def pick_speed(self, fast_speed, mid_speed, slow_speed):
        if self.go_fast:
            if not self.go_slow:
                return fast_speed
        elif self.go_slow:
            return slow_speed
        return mid_speed