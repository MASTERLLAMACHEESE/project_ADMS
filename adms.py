import sys
import time
import module
from pydub import AudioSegment
from pydub.playback import play
import threading


class Pad:

    def __init__(self):
        pass

    def select_sound(self, btn):
        module.pad_selected = btn

    def play_sound(self, btn):
        play(module.sounds[btn])

    def load_sounds(self):
        for i in range(16):
            try:
                sound = AudioSegment.from_wav(f"/media/usb/{str(i+1)}.wav")
                module.sound_path = '/media/usb'
            except FileNotFoundError:
                sound = AudioSegment.from_wav(f"./sounds/{str(i + 1)}.wav")
                module.sound_path = './sounds'
            module.sounds.append(sound)
        module.usb_sounds = module.sounds

    def toggle_pitch_mode(self):
        if not module.selected:
            print(f'{module.current_time()} Please select a sound first')
            return

        if module.pitch_mode:
            module.sounds = module.usb_sounds
            module.pitch_mode = False
            return

        module.pitch_mode = True
        out_sounds = []
        octaves = 2
        for i in range(16):
            new_sample_rate = int(module.usb_sounds[module.selected].frame_rate * (2.0 ** octaves))
            sound_resample = module.usb_sounds[module.selected]._spawn(module.usb_sounds[module.selected].raw_data,
                                                                       overrides={'frame_rate': new_sample_rate})
            out_sounds.append(sound_resample)
            octaves -= 0.1
        module.sounds = out_sounds


def sequencer_loop():
    while module.seq_loop is True:
        for i in range(16):
            prev = time.time()
            sounds = module.sounds_in_beat[i]
            mixed = None
            if len(sounds) == 4:
                mixed = sounds[0].overlay(sounds[1]).overlay(sounds[2]).overlay(sounds[3])
            if len(sounds) == 3:
                mixed = sounds[0].overlay(sounds[1]).overlay(sounds[2])
            if len(sounds) == 2:
                mixed = sounds[0].overlay(sounds[1])
            if len(sounds) == 1:
                mixed = sounds[0]

            if mixed:
                play(mixed)

            sys_delay = time.time() - prev
            time.sleep(module.delay - (sys_delay if sys_delay < module.delay else module.delay))


class Sequencer:

    def __init__(self, start=False):
        module.delay = 60 / module.bpm
        self.seq_thread = threading.Thread(target=sequencer_loop)
        if start:
            self.start()

    def start(self):
        print(f'\n{module.current_time()} Starting sequencer\n'
              f'{module.current_time()} Please wait...')
        module.seq_loop = True
        time.sleep(1)
        self.seq_thread = threading.Thread(target=sequencer_loop)
        self.seq_thread.start()
        print(f'{module.current_time()} Sequencer ready\n')

    def stop(self):
        print(f'\n{module.current_time()} Terminating sequencer\n'
              f'{module.current_time()} Please wait...')
        module.seq_loop = False
        self.seq_thread.join()
        module.sounds_in_beat = [[] for y in range(16)]
        print(f'{module.current_time()} Sequencer stopped\n')

    def toggle_play(self):
        if module.seq_loop:
            self.stop()
        else:
            self.start()
        print(f'{module.current_time()} Currently active threads: {threading.active_count()}')

    def toggle_sound(self, index, sound):
        if sound not in module.sounds_in_beat[index]:
            module.sounds_in_beat[index].append(sound)
        else:
            module.sounds_in_beat[index].remove(sound)
        time.sleep(0.3)

    def change_bpm(self, value):
        if value == 124:
            module.bpm = 124
        else:
            module.bpm += value

        module.delay = (60 / module.bpm) / 2
        print(f'{module.current_time()} Current bpm: {module.bpm}')


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
