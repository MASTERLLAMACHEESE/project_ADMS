import RPi.GPIO as GPIO
import time
import _thread
from controller import Controller
# https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.raspberrypi.org%2Fdocumentation%2Fusage%2Fgpio%2F&psig=AOvVaw0ngttCGDmViun_dXn9x-9a&ust=1604311768285000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJidkZyN4ewCFQAAAAAdAAAAABAO
# 4x4 pad io
PAD_L1 = 19
PAD_L2 = 13
PAD_L3 = 6
PAD_L4 = 5
PAD_C1 = 12
PAD_C2 = 16
PAD_C3 = 20
PAD_C4 = 21

# sequencer io
SEQ_L1 = 4
SEQ_L2 = 17
SEQ_L3 = 27
SEQ_L4 = 22
SEQ_C1 = 18
SEQ_C2 = 23
SEQ_C3 = 24
SEQ_C4 = 25

# play/pause btn
P_IN = 9
P_OUT = 10

controller = Controller()


# 4x4 pad init
def pad_init():
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


def seq_init():
    GPIO.setup(SEQ_L1, GPIO.OUT)
    GPIO.setup(SEQ_L2, GPIO.OUT)
    GPIO.setup(SEQ_L3, GPIO.OUT)
    GPIO.setup(SEQ_L4, GPIO.OUT)

    GPIO.setup(SEQ_C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SEQ_C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SEQ_C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SEQ_C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def play_init():
    GPIO.setup(P_OUT, GPIO.OUT)
    GPIO.setup(P_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def read_line(line, key, btn_type):
    GPIO.output(line, GPIO.HIGH)
    if btn_type == 'pad':
        if GPIO.input(PAD_C1) == 1:
            controller.input('pad', key[0])
        if GPIO.input(PAD_C2) == 1:
            controller.input('pad', key[1])
        if GPIO.input(PAD_C3) == 1:
            controller.input('pad', key[2])
        if GPIO.input(PAD_C4) == 1:
            controller.input('pad', key[3])
    if btn_type == 'seq':
        if GPIO.input(SEQ_C1) == 1:
            controller.input('seq', key[0])
        if GPIO.input(SEQ_C2) == 1:
            controller.input('seq', key[1])
        if GPIO.input(SEQ_C3) == 1:
            controller.input('seq', key[2])
        if GPIO.input(SEQ_C4) == 1:
            controller.input('seq', key[3])
    if btn_type == 'play':
        if GPIO.input(P_IN) == 1:
            controller.input('play', 1)
    GPIO.output(line, GPIO.LOW)


def buttons():
    while True:
        read_line(PAD_L1, [1, 2, 3, 4], 'pad')
        read_line(PAD_L2, [5, 6, 7, 8], 'pad')
        read_line(PAD_L3, [9, 10, 11, 12], 'pad')
        read_line(PAD_L4, [13, 14, 15, 16], 'pad')

        read_line(SEQ_L1, [1, 5, 9, 13], 'seq')
        read_line(SEQ_L2, [2, 6, 10, 14], 'seq')
        read_line(SEQ_L3, [3, 7, 11, 15], 'seq')
        read_line(SEQ_L4, [4, 8, 12, 16], 'seq')

        read_line(P_OUT, [1], 'play')

        time.sleep(0.2)


try:
    pad_init()
    seq_init()
    play_init()
    _thread.start_new_thread(buttons, ())
    while 1:
        continue
except KeyboardInterrupt:
    print("\nApplication stopped")
