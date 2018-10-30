from animation import Animation
from time import sleep
from cozmo.util import degrees, radians, distance_mm, speed_mmps, Pose

class Cube(Animation):
    def Draw(self):
        self.Ready()
        sleep(0.5)
        self.LiftUp()
        sleep(1)

        # self.cozmo.go_to_pose(Pose(100, 100, 0), relative_to_robot=False).wait_for_completed()
        # self.cozmo.turn_in_place(degrees(-90)).wait_for_completed()
        # self.LiftDown()
        # self.cozmo.go_to_pose(Pose(100, -100, 0), relative_to_robot=False).wait_for_completed()
        # self.LiftUp()
        # self.cozmo.turn_in_place(degrees(-90)).wait_for_completed()

        self.LiftDown()
        sleep(0.1)
        for _ in range(16):
            self.cozmo.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
            self.cozmo.turn_in_place(degrees(90)).wait_for_completed()
        self.LiftUp()