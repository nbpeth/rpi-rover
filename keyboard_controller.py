from pynput import keyboard

DIAGONAL_UP_LEFT = "DIAGONAL_UP_LEFT"
DIAGONAL_UP_RIGHT = "DIAGONAL_UP_RIGHT"
DIAGONAL_DOWN_LEFT = "DIAGONAL_DOWN_LEFT"
DIAGONAL_DOWN_RIGHT = "DIAGONAL_DOWN_RIGHT"
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

DIRECTIONS = {
    DIAGONAL_UP_LEFT: frozenset({keyboard.Key.up, keyboard.Key.left}),
    DIAGONAL_UP_RIGHT: frozenset({keyboard.Key.up, keyboard.Key.right}),
    DIAGONAL_DOWN_LEFT: frozenset({keyboard.Key.down, keyboard.Key.left}),
    DIAGONAL_DOWN_RIGHT: frozenset({keyboard.Key.down, keyboard.Key.right}),
    UP: frozenset({keyboard.Key.up}),
    DOWN: frozenset({keyboard.Key.down}),
    LEFT: frozenset({keyboard.Key.left}),
    RIGHT: frozenset({keyboard.Key.right}),
}

QUIT_KEY = keyboard.Key.esc

FULL_SPEED = 1
CURVE_SPEED = 0.5


class KeyboardController:
    def __init__(self, robot):
        self.pressed_keys = set()
        self.robot = robot

    def is_pressed(self, direction):
        return DIRECTIONS[direction].issubset(self.pressed_keys)

    def on_press(self, key):
        self.pressed_keys.add(key)
        if self.is_pressed(DIAGONAL_UP_LEFT):
            print(f"key: {DIAGONAL_UP_LEFT}")
            self.robot.left_motor.forward(FULL_SPEED)
            self.robot.right_motor.forward(CURVE_SPEED)
        elif self.is_pressed(DIAGONAL_UP_RIGHT):
            print(f"key: {DIAGONAL_UP_RIGHT}")
            self.robot.left_motor.forward(CURVE_SPEED)
            self.robot.right_motor.forward(FULL_SPEED)
        elif self.is_pressed(DIAGONAL_DOWN_LEFT):
            print(f"key: {DIAGONAL_DOWN_LEFT}")
            self.robot.left_motor.forward(CURVE_SPEED)
            self.robot.right_motor.forward(FULL_SPEED)
        elif self.is_pressed(DIAGONAL_DOWN_RIGHT):
            print(f"key: {DIAGONAL_DOWN_RIGHT}")
            self.robot.left_motor.forward(FULL_SPEED)
            self.robot.right_motor.forward(CURVE_SPEED)
        elif self.is_pressed(UP):
            print(f"key: {UP}")
            self.robot.forward()
        elif self.is_pressed(DOWN):
            print(f"key: {DOWN}")
            self.robot.backward()
        elif self.is_pressed(LEFT):
            print(f"key: {LEFT}")
            self.robot.left()
        elif self.is_pressed(RIGHT):
            print(f"key: {RIGHT}")
            self.robot.right()

    def on_release(self, key):
        self.pressed_keys.discard(key)
        if key == QUIT_KEY:
            return False

    def listen(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
