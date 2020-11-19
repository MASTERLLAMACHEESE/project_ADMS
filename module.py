import datetime

sound_path = None
is_usb = False
bpm = 124
sounds = []
usb_sounds = []
sounds_in_beat = [
    [sounds[0], sounds[5], sounds[7]],
    [sounds[0], sounds[7]],
    [sounds[0], sounds[5], sounds[7]],
    [sounds[0], sounds[7]],
    [sounds[0], sounds[5], sounds[7]],
    [sounds[0], sounds[7]],
    [sounds[0], sounds[5], sounds[7]],
    [sounds[0], sounds[7]],
    [sounds[0], sounds[5], sounds[7]],
    [sounds[0], sounds[7]],
    [sounds[0], sounds[5], sounds[7]],
    [sounds[0], sounds[7]],
    [sounds[0], sounds[5], sounds[7]],
    [sounds[0], sounds[7]],
    [sounds[0], sounds[5], sounds[7]],
    [sounds[0], sounds[7]],

]
seq_loop = False
pad_selected = None
selected = None
delay = None
pitch_mode = False

pressed_key = (None, None)


def current_time():
    return f'[{datetime.datetime.now().strftime("%H:%M:%S")}]'
