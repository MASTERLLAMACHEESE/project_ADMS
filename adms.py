import sys
import threading
import module
import pygame
from pad import Pad
from sequencer import Sequencer
import pc_inputs
# import rasp_inputs

pygame.mixer.init()
module.sound_path = f'./sounds'
pad = Pad()
sequencer = Sequencer()


def pressed_key(key):
    value, btn_type = key
    if btn_type == 'seq':
        if module.selected:
            sequencer.toggle_sound(value-1, module.sounds[module.selected])
    if btn_type == 'pad':
        module.selected = value
        pad.play_sound(value)
    if btn_type == 'bpm':
        sequencer.change_bpm(value)
    if btn_type == 'pitch':
        pad.toggle_pitch_mode()
    if btn_type == 'play':
        sequencer.toggle_play()


def pc_init():
    pc_inputs.start_listener()


def rasp_init():
    pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(f'Please provide either "pc" or "rasp" when running this file')
    if len(sys.argv) > 2:
        sys.exit(f'Too many arguments passed: expected 1, got {len(sys.argv)-1}')
    if sys.argv[1] != 'pc' and sys.argv[1] != 'rasp':
        sys.exit(f'Incorrect argument passed: {sys.argv[1]}\n'
                 f'Please provide either "pc" or "rasp" when running this file')

    if sys.argv[1] == 'pc':
        pc_init()
    if sys.argv[1] == 'rasp':
        rasp_init()

    pad.load_sounds()

    while True:
        pass
