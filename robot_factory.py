from fakebot import FakeBot
import os
from gpiozero import Robot, Motor

class RobotFactory:
    @staticmethod
    def get_robot():
        if os.getenv("ENV") == "dev":
            print("Running in development mode. Using FakeBot.")
            return FakeBot()
        else:
            LEFT_WHEEL_PINS = {"forward": 20, "backward": 21, "enable": 12}
            RIGHT_WHEEL_PINS = {"forward": 6, "backward": 5, "enable": 13}
            return Robot(left=Motor(**LEFT_WHEEL_PINS), right=Motor(**RIGHT_WHEEL_PINS))