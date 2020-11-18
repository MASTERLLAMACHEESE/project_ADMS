import RPi.GPIO as GPIO
import threading
import module

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


def read_line(line, key):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(PAD_C1) == 1:
        module.pressed_key = key[0]
    if GPIO.input(PAD_C2) == 1:
        module.pressed_key = key[1]
    if GPIO.input(PAD_C3) == 1:
        module.pressed_key = key[2]
    if GPIO.input(PAD_C4) == 1:
        module.pressed_key = key[3]
    if GPIO.input(SEQ_C1) == 1:
        module.pressed_key = key[0]
    if GPIO.input(SEQ_C2) == 1:
        module.pressed_key = key[1]
    if GPIO.input(SEQ_C3) == 1:
        module.pressed_key = key[2]
    if GPIO.input(SEQ_C4) == 1:
        module.pressed_key = key[3]
    if GPIO.input(P_IN) == 1:
        module.pressed_key = key[0]
    GPIO.output(line, GPIO.LOW)


def buttons():
    while True:
        read_line(PAD_L1, [(1, 'pad'), (2, 'pad'), (3, 'pad'), (4, 'pad')])
        read_line(PAD_L2, [(5, 'pad'), (6, 'pad'), (7, 'pad'), (8, 'pad')])
        read_line(PAD_L3, [(9, 'pad'), (10, 'pad'), (11, 'pad'), (12, 'pad')])
        read_line(PAD_L4, [(13, 'pad'), (14, 'pad'), (15, 'pad'), (16, 'pad')])

        read_line(SEQ_L1, [(1, 'seq'), (5, 'seq'), (9, 'seq'), (13, 'seq')])
        read_line(SEQ_L2, [(2, 'seq'), (6, 'seq'), (10, 'seq'), (14, 'seq')])
        read_line(SEQ_L3, [(3, 'seq'), (7, 'seq'), (11, 'seq'), (15, 'seq')])
        read_line(SEQ_L4, [(4, 'seq'), (8, 'seq'), (12, 'seq'), (16, 'seq')])

        read_line(P_OUT, [(13, 'play')])


def start_listener():
    pad_init()
    seq_init()
    play_init()
    listener = threading.Thread(target=buttons)
    listener.start()
