import RPi.GPIO as GPIO
import time
import _thread
from .controller import Controller

# 4x4 pad io
PAD_L1 = 19
PAD_L2 = 13
PAD_L3 = 6
PAD_L4 = 5
PAD_C1 = 12
PAD_C2 = 16
PAD_C3 = 20
PAD_C4 = 21

controller = Controller()


# 4x4 pad init
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(PAD_L1, GPIO.OUT)
    GPIO.setup(PAD_L2, GPIO.OUT)
    GPIO.setup(PAD_L3, GPIO.OUT)
    GPIO.setup(PAD_L4, GPIO.OUT)

    GPIO.setup(PAD_C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PAD_C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PAD_C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PAD_C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def read_line(line, key):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(PAD_C1) == 1:
        controller.execute(key[0])
    if GPIO.input(PAD_C2) == 1:
        controller.execute(key[1])
    if GPIO.input(PAD_C3) == 1:
        controller.execute(key[2])
    if GPIO.input(PAD_C4) == 1:
        controller.execute(key[3])
    GPIO.output(line, GPIO.LOW)


def sound_pad():
    while True:
        read_line(PAD_L1, [1, 2, 3, 4])
        read_line(PAD_L2, [5, 6, 7, 8])
        read_line(PAD_L3, [9, 10, 11, 12])
        read_line(PAD_L4, [13, 14, 15, 16])
        time.sleep(0.1)


try:
    init()
    _thread.start_new_thread(sound_pad, ())
    while 1:
        continue
except KeyboardInterrupt:
    print("\nApplication stopped")
