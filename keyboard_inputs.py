from controller import Controller
from pynput import keyboard

sequencer_mapping = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    'q': 5,
    'w': 6,
    'e': 7,
    'r': 8,
    'a': 9,
    's': 10,
    'd': 11,
    'f': 12,
    'z': 13,
    'x': 14,
    'c': 15,
    'v': 16,
}

pad_mapping = {
    '7': 1,
    '8': 2,
    '9': 3,
    '0': 4,
    'u': 5,
    'i': 6,
    'o': 7,
    'p': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'ö': 12,
    'm': 13,
    ',': 14,
    '.': 15,
    '-': 16,
}

controller = Controller()


def on_press(key):
    try:
        print(key.char)
        seq_btn = sequencer_mapping.get(key.char)
        pad_btn = pad_mapping.get(key.char)
        if seq_btn:
            controller.input('seq', seq_btn)
        if pad_btn:
            controller.input('pad', pad_btn)
    except AttributeError:
        pass


listener = keyboard.Listener(
    on_press=on_press
)
listener.start()

while True:
    continue
