"""
ToDo figure out what variables don't really need to be here
All variables for communication between classes and files
"""
import datetime

sound_path = None
bpm = 175
sounds = []  # Sounds that can be added to sequencer loop
usb_sounds = []  # Raw sounds from either USB or .sounds folder
sounds_in_beat = [[] for y in range(16)]  # Sequencer plays sounds form this list, pretty much a 16x4 matrix
seq_loop = False  # Sequencer on/off
selected = None  # Selected sound gets saved here
delay = None  # Delay between every beat, gets calculated in Sequencer()
pitch_mode = False  # Pitch mode on/off
playback = True  # Pad playback on/off
blink_led = False  # Currently not used, can be used to blink leds when a sound plays in a sequencer beat
current_beat = None  # Sequencer current beat, used for leds
pressed_key = (None, None)  # If a key gets pressed, the value type tuple gets saved here

pos_in_seq = []  # When Pad button is pressed, its positions in sequencer will be saved here, used for leds
pad_clicked = False

# led indexes
seq_led = 16
pitch_led = 17
playback_led = 18
seq_leds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def current_time():
    """
    Useful for debugging with prints/logs. Adds time in front of every print
    print(f'{module.current_time} <your_text_here>')
    """
    return f'[{datetime.datetime.now().strftime("%H:%M:%S")}]'
