#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback
from pynput import keyboard
import module

key_mappings = {
    # Sequencer keys
    '1': (1, 'seq'),
    '2': (2, 'seq'),
    '3': (3, 'seq'),
    '4': (4, 'seq'),
    'q': (5, 'seq'),
    'w': (6, 'seq'),
    'e': (7, 'seq'),
    'r': (8, 'seq'),
    'a': (9, 'seq'),
    's': (10, 'seq'),
    'd': (11, 'seq'),
    'f': (12, 'seq'),
    'z': (13, 'seq'),
    'x': (14, 'seq'),
    'c': (15, 'seq'),
    'v': (16, 'seq'),
    # Pad keys
    '7': (1, 'pad'),
    '8': (2, 'pad'),
    '9': (3, 'pad'),
    '0': (4, 'pad'),
    'u': (5, 'pad'),
    'i': (6, 'pad'),
    'o': (7, 'pad'),
    'p': (8, 'pad'),
    'j': (9, 'pad'),
    'k': (10, 'pad'),
    'l': (11, 'pad'),
    'ö': (12, 'pad'),
    'm': (13, 'pad'),
    ',': (14, 'pad'),
    '.': (15, 'pad'),
    '-': (16, 'pad'),
    # BPM keys
    'y': (1, 'bpm'),
    'h': (-1, 'bpm'),
    'n': (124, 'bpm'),
    # Pitch select key
    't': (1, 'pitch'),
    # Play toggle
    'g': (1, 'play'),
}


def on_press(key):
    try:
        mapped_key = key_mappings.get(key.char)
        if mapped_key:
            module.pressed_key = mapped_key
    except AttributeError:
        traceback.print_exc()
    except KeyboardInterrupt:
        print(f"\n{module.current_time()} Application stopped")


def start_listener():

    listener = keyboard.Listener(
        on_press=on_press
    )
    listener.start()
