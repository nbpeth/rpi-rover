from time import sleep
from keyboard_controller import KeyboardController
from robot_factory import RobotFactory

try:
    keyboard_controller = KeyboardController(robot=RobotFactory.get_robot())
    keyboard_controller.listen()
    
except Exception as e:
    print(f"Error initializing robot: {e}")
    



