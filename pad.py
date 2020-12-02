import module
from pydub.playback import play
from pydub import AudioSegment
import threading
import time


class Pad:

    def __init__(self):
        pass

    def select_sound(self, btn):
        module.pad_selected = btn

    def play_sound(self, btn):
        threading.Thread(target=play, args=(module.sounds[btn],)).start()
        time.sleep(0.1)

    def load_sounds(self):
        for i in range(16):
            try:
                sound = AudioSegment.from_wav(f"/media/usb/{str(i+1)}.wav")
                module.sound_path = '/media/usb'
            except FileNotFoundError:
                sound = AudioSegment.from_wav(f"./sounds/{str(i+1)}.wav")
                module.sound_path = './sounds'
            module.sounds.append(sound)
        module.usb_sounds = module.sounds
        print(f'{module.current_time()} Sounds path: {module.sound_path}')

    def toggle_pitch_mode(self):
        if not module.selected:
            print(f'{module.current_time()} Please select a sound first')
            time.sleep(0.3)
            return

        if module.pitch_mode:
            module.sounds = module.usb_sounds
            module.pitch_mode = False
            time.sleep(0.3)
            return

        module.pitch_mode = True
        out_sounds = []
        octaves = 2
        for i in range(16):
            new_sample_rate = int(module.usb_sounds[module.selected-1].frame_rate * (2.0 ** octaves))
            sound_resample = module.usb_sounds[module.selected-1]._spawn(module.usb_sounds[module.selected-1].raw_data,
                                                                         overrides={'frame_rate': new_sample_rate})
            sound = sound_resample.set_frame_rate(44100)
            out_sounds.append(sound)
            octaves -= 0.1
        module.sounds = out_sounds
        time.sleep(0.3)
