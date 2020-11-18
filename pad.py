import module
from pydub.playback import play
from sound import Sound


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
                sound = Sound(f"/media/usb/{str(i+1)}.wav")
                module.sound_path = '/media/usb'
            except FileNotFoundError:
                sound = Sound(f"./sounds/{str(i + 1)}.wav")
                module.sound_path = './sounds'
            sound.pad_pos = i
            module.sounds.append(sound.sound)
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
