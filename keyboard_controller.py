from key_input import UP, DOWN, LEFT, RIGHT, listen as listen_for_keys

DIAGONAL_UP_LEFT = "DIAGONAL_UP_LEFT"
DIAGONAL_UP_RIGHT = "DIAGONAL_UP_RIGHT"
DIAGONAL_DOWN_LEFT = "DIAGONAL_DOWN_LEFT"
DIAGONAL_DOWN_RIGHT = "DIAGONAL_DOWN_RIGHT"

DIRECTIONS = {
    DIAGONAL_UP_LEFT: frozenset({UP, LEFT}),
    DIAGONAL_UP_RIGHT: frozenset({UP, RIGHT}),
    DIAGONAL_DOWN_LEFT: frozenset({DOWN, LEFT}),
    DIAGONAL_DOWN_RIGHT: frozenset({DOWN, RIGHT}),
    UP: frozenset({UP}),
    DOWN: frozenset({DOWN}),
    LEFT: frozenset({LEFT}),
    RIGHT: frozenset({RIGHT}),
}

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
        if not self.pressed_keys:
            print("key: STOP")
            self.robot.stop()

    def listen(self):
        try:
            listen_for_keys(self.on_press, self.on_release)
        finally:
            self.robot.stop()
