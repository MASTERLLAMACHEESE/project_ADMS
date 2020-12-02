import time

import RPi.GPIO as GPIO
import threading
import module
# https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.raspberrypi.org%2Fdocumentation%2Fusage%2Fgpio%2F&psig=AOvVaw0ngttCGDmViun_dXn9x-9a&ust=1604311768285000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJidkZyN4ewCFQAAAAAdAAAAABAO


# 6x6 button matrix pins
ROW = [26, 19, 13, 6, 5, 0]
COL = [21, 20, 16, 12, 1, 7]

# Every button definiton in the 6x6 matrix
DEFINITIONS = [
    [(4, 'pad'), (3, 'pad'), (2, 'pad'), (1, 'pad'), (8, 'pad'), (7, 'pad')],
    [(6, 'pad'), (5, 'pad'), (12, 'pad'), (11, 'pad'), (10, 'pad'), (9, 'pad')],
    [(16, 'pad'), (15, 'pad'), (14, 'pad'), (13, 'pad'), (1, 'seq'), (2, 'seq')],
    [(3, 'seq'), (4, 'seq'), (5, 'seq'), (6, 'seq'), (7, 'seq'), (8, 'seq')],
    [(9, 'seq'), (10, 'seq'), (11, 'seq'), (12, 'seq'), (13, 'seq'), (14, 'seq')],
    [(15, 'seq'), (16, 'seq'), (1, 'play'), (1, 'pitch'), (None, ''), (None, '')],
]

# Joystick pins
JOYSTICK = [2, 3, 4, 17, 27, 22, 10]

# Joystick buttons definition
JS_DEF = [(None, ''), (None, ''), (-1, 'bpm'), (1, 'bpm'), (124, 'bpm'), (1, 'playback'), (None, '')]


# setup GPIO and pin definitions
def btns_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # All pins in ROW are outputs
    for pin in ROW:
        GPIO.setup(pin, GPIO.OUT)

    # All pins in COL are inputs
    for pin in COL:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # All JOYSTICK pins are inputs
    for pin in JOYSTICK:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Reads input pins on given ROW
def read_inputs(row, map):
    GPIO.output(row, GPIO.HIGH)
    for index, col in enumerate(COL):
        if GPIO.input(col) == 1:
            module.pressed_key = map[index]
    GPIO.output(row, GPIO.LOW)


# Outputs 3.3v on every ROW one by one /w delay
def buttons():
    try:
        while True:
            for index, row in enumerate(ROW):
                read_inputs(row, DEFINITIONS[index])
                time.sleep(0.01)

            for index, btn in enumerate(JOYSTICK):
                if not GPIO.input(btn):
                    module.pressed_key = JS_DEF[index]
    except KeyboardInterrupt:
        return


# Starts a thread that checks pins
def start_listener():
    btns_init()
    listener = threading.Thread(target=buttons)
    listener.start()
