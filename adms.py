import sys
import time
import module
from pad import Pad
from sequencer import Sequencer

pad = Pad()
sequencer = Sequencer()


def clear_pressed_key():
    module.pressed_key = (None, None)
    time.sleep(0.1)


def check_pressed_key():
    value, btn_type = module.pressed_key
    if btn_type == 'seq':
        if module.selected:
            sequencer.toggle_sound(value-1, module.sounds[module.selected])
            clear_pressed_key()
    if btn_type == 'pad':
        module.selected = value
        pad.play_sound(value)
        clear_pressed_key()
    if btn_type == 'bpm':
        sequencer.change_bpm(value)
        clear_pressed_key()
    if btn_type == 'pitch':
        pad.toggle_pitch_mode()
        clear_pressed_key()
    if btn_type == 'play':
        sequencer.toggle_play()
        clear_pressed_key()


def pc_init():
    from pc_inputs import start_listener
    start_listener()


def rasp_init():
    from rasp_inputs import start_listener
    start_listener()


if len(sys.argv) < 2:
    sys.exit(f'{module.current_time()} Please provide either "pc" or "rasp" when running this file')
if len(sys.argv) > 2:
    sys.exit(f'{module.current_time()} Too many arguments passed: expected 1, got {len(sys.argv)-1}')
if sys.argv[1] != 'pc' and sys.argv[1] != 'rasp':
    sys.exit(f'{module.current_time()} Incorrect argument passed: {sys.argv[1]}\n'
             f'{module.current_time()} Please provide either "pc" or "rasp" when running this file')

if sys.argv[1] == 'pc':
    pc_init()
if sys.argv[1] == 'rasp':
    rasp_init()

pad.load_sounds()

while True:
    check_pressed_key()
