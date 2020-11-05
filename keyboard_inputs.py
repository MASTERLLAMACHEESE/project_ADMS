#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller import Controller
from pitch import Pitch
import _thread
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

bpm_mapping = {
    'y': 1,
    'h': 2,
    'n': 3,
}
#simple solution is to check press resample sound in 16 ways and map to 4x4 buttons
#when repressed reset and take original 16 sounds back to board
pitch_mapping = {
    't': 1,
}

controller = Controller()
pitch = Pitch()
controller.seq_toggle_play()


def on_press(key):
    try:
        print(key.char)
        seq_btn = sequencer_mapping.get(key.char)
        pad_btn = pad_mapping.get(key.char)
        bpm_btn = bpm_mapping.get(key.char)
        pitch_btn = pitch_mapping.get(key.char)
        if seq_btn:
            controller.input(seq_btn, 'seq')
        if pad_btn:
            controller.input(pad_btn, 'pad')
        if bpm_btn:
            controller.input(bpm_btn, 'bpm')
        if pitch_btn:
            pitch.input(pitch_btn,'pitch')
    except AttributeError:
        pass


listener = keyboard.Listener(
    on_press=on_press
)
listener.start()

while True:
    continue
