from gpiozero import Device

class FakeMotor(Device):
    def __init__(self, name):
        self.name = name
        print(f"FakeMotor initialized with name: {self.name}")

    def forward(self, speed=1):
        print(f"FakeMotor {self.name} moving forward at speed {speed}")

    def backward(self, speed=1):
        print(f"FakeMotor {self.name} moving backward at speed {speed}")

    def stop(self):
        print(f"FakeMotor {self.name} stopped")

class FakeBot(Device):
    def __init__(self):
        print("FakeBot initialized")
        self.left_motor = FakeMotor("left")
        self.right_motor = FakeMotor("right")

    def forward(self, speed=1):
        print(f"Moving forward at speed {speed}")

    def backward(self, speed=1):
        print(f"Moving backward at speed {speed}")

    def left(self, speed=1):
        print(f"Turning left at speed {speed}")

    def right(self, speed=1):
        print(f"Turning right at speed {speed}")

    def stop(self):
        print("Stopping")
