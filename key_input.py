import os
import select
import sys
import termios
import time

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

ARROWS = {"A": UP, "B": DOWN, "C": RIGHT, "D": LEFT}

HOLD_TIMEOUT = 0.25  
POLL_INTERVAL = 0.02


def listen(on_press, on_release):
    """Block until Esc or q, calling on_press/on_release with UP/DOWN/LEFT/RIGHT."""
    if not sys.stdin.isatty():
        raise RuntimeError("keyboard control needs a terminal")

    fd = sys.stdin.fileno()
    original = termios.tcgetattr(fd)
    raw = termios.tcgetattr(fd)
    raw[3] &= ~(termios.ECHO | termios.ICANON)  
    raw[6][termios.VMIN] = 0
    raw[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSADRAIN, raw)

    held = None
    last_seen = 0.0
    try:
        while True:
            if select.select([fd], [], [], POLL_INTERVAL)[0]:
                data = os.read(fd, 32).decode("utf-8", "ignore")
                if not data or data in ("q", "Q", "\x03", "\x1b"):
                    return
                key = ARROWS.get(data[-1]) if data.startswith("\x1b") else None
                if key:
                    if key != held:
                        if held:
                            on_release(held)
                        on_press(key)
                        held = key
                    last_seen = time.monotonic()
            if held and time.monotonic() - last_seen > HOLD_TIMEOUT:
                on_release(held)
                held = None
    finally:
        if held:
            on_release(held)
        termios.tcsetattr(fd, termios.TCSADRAIN, original)
