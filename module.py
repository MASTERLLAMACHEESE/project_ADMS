import datetime

sound_path = None
is_usb = False
bpm = 124
sounds = []
usb_sounds = []
sounds_in_beat = [[] for y in range(16)]
seq_loop = False
pad_selected = None
selected = None
delay = None
pitch_mode = False
# delay = int((60 / bpm * 1000))


def current_time():
    return f'[{datetime.datetime.now().strftime("%H:%M:%S")}]'
