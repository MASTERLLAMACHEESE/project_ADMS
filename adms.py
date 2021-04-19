import sys
import time
import module
from pad import Pad
from sequencer import Sequencer
import main_gui

pad = Pad()
sequencer = Sequencer()


def clear_pressed_key():
    module.pressed_key = (None, None)
    time.sleep(0.1)


def check_pressed_key():
    """
    Get pressed key value from module and to something with it
    """
    value, btn_type = module.pressed_key
    if btn_type == 'seq':
        gui_seq().seq_value(value)
        if module.selected:
            sequencer.toggle_sound(value-1, module.sounds[module.selected-1])  # add or remove sound

    if btn_type == 'pad':
        module.selected = value  # selected sound value
        gui_seq().pad_value(value)
        for i, beat in enumerate(module.sounds_in_beat):  # checks if sound is already in sequencer
            if module.sounds[value-1] in beat:
                module.pos_in_seq.append(i)
        module.pad_clicked = True  # pad was clicked
        if module.playback:
            pad.play_sound(value-1)  # Play sound

    if btn_type == 'bpm':
        sequencer.change_bpm(value)  # Change BPM

    if btn_type == 'pitch':
        pad.toggle_pitch_mode()  # Toggle pitch mode

    if btn_type == 'play':
        sequencer.toggle_play()  # Toggle sequencer

    if btn_type == 'playback':
        module.playback = not module.playback  # Toggle pad sound playback
        print(f'{module.current_time()} Playback {"enabled" if module.playback else "disabled"}')
        time.sleep(0.3)
    clear_pressed_key()


def pc_init():
    """
    Starts PC specific threads
    """
    from pc_inputs import start_listener
    #from main_gui import main
    start_listener()
    #main()


def rasp_init():
    """
    Starts raspberry specific threads
    """
    from led import start_led
    from rasp_inputs import start_listener
    #from main_gui import start_gui
    start_listener()
    start_led()
    #start_gui()



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

pad.load_sounds()  # ToDo maybe this need to happen on Pad() init?

while True:
    check_pressed_key()


class gui_seq():
    """
    Create data for gui sequencer
    """

    pad_mapping = {
        # Pad keys
        4:"Kick 1",
        3:"Kick 2",
        2:"Kick 3",
        1:"Kick 4",
        8:"Snare 1",
        7:"Snare 2",
        6:"Snare 3",
        5:"Clap 1",
        12:"Closed Hat 1",
        11:"Closed Hat 2",
        10:"Closed Hat 3",
        9:"Closed Hat 4",
        16:"Closed hat 5",
        15:"Crash 1",
        14:"Tom 1",
        13:"Floot Tom 1"
    }

    def pad_value(self, value):
        self.pad_btn = value
    
    def seq_value(self, value):
        self.seq_btn = value

    def create_list(self):
        #create list to store in seq_btn place, pat_btn values word
        for e in gui_seq.pad_mapping:
            if e not in module.gui_list[module.pos_in_seq]:
                if len(module.gui_list[module.pos_in_seq]) < 4:
                    module.gui_list[module.pos_in_seq].append(e)
            else:
                module.gui_list[module.pos_in_seq].remove(e)
