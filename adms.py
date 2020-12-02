import sys
import time
import module
from pad import Pad
from sequencer import Sequencer
from led import start_led
from ambient_led import start_ambient

pad = Pad()
sequencer = Sequencer()


def clear_pressed_key():
    module.pressed_key = (None, None)
    time.sleep(0.1)


def check_pressed_key():
    value, btn_type = module.pressed_key
    if btn_type == 'seq':
        if module.selected:
            sequencer.toggle_sound(value-1, module.sounds[module.selected-1])
    if btn_type == 'pad':
        module.selected = value
        if module.playback:
            pad.play_sound(value-1)
    if btn_type == 'bpm':
        sequencer.change_bpm(value)
    if btn_type == 'pitch':
        pad.toggle_pitch_mode()
    if btn_type == 'play':
        sequencer.toggle_play()
    if btn_type == 'playback':
        module.playback = not module.playback
        print(f'{module.current_time()} Playback {"enabled" if module.playback else "disabled"}')
        time.sleep(0.3)
    clear_pressed_key()


def pc_init():
    from pc_inputs import start_listener
    start_listener()


def rasp_init():
    from rasp_inputs import start_listener
    start_listener()
    start_led()


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
