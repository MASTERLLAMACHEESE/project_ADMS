import datetime
from pydub import AudioSegment
sound_path = None
is_usb = False
bpm = 124
sounds = []
usb_sounds = []
silence = AudioSegment.silent(duration=1)
sounds_in_beat = [[silence for x in range(4)] for y in range(16)]
seq_loop = False
pad_selected = None
selected = None
delay = None
pitch_mode = False
# delay = int((60 / bpm * 1000))

pressed_key = (None, None)


def current_time():
    return f'[{datetime.datetime.now().strftime("%H:%M:%S")}]'
