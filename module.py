import datetime

sound_path = None
is_usb = False
bpm = 175
sounds = []
usb_sounds = []
sounds_in_beat = [[] for y in range(16)]
seq_loop = False
pad_selected = None
selected = None
delay = None
pitch_mode = False
playback = True
blink_led = False
current_beat = None
pressed_key = (None, None)

pos_in_seq = []
pad_clicked = False

seq_led = 16
pitch_led = 17
playback_led = 18
seq_leds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def current_time():
    return f'[{datetime.datetime.now().strftime("%H:%M:%S")}]'
