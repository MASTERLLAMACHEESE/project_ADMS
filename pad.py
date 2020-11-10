import module
import pygame
from sound import Sound
from samplerate import resample


class Pad:

    def __init__(self):
        pass

    def select_sound(self, btn):
        module.pad_selected = btn

    def play_sound(self, btn):
        module.sounds[btn].play()

    def load_sounds(self):
        for i in range(16):
            sound = Sound(f"{module.sound_path}/{str(i+1)}.wav")
            sound.pad_pos = i
            module.sounds.append(sound.sound)
        module.usb_sounds = module.sounds

    def toggle_pitch_mode(self):
        if not module.selected:
            print(f'Please select a sound first')
            return

        if module.pitch_mode:
            module.sounds = module.usb_sounds
            module.pitch_mode = False
            return

        module.pitch_mode = True
        sound_array = pygame.sndarray.array(module.usb_sounds[module.selected])
        out_sounds = []
        ratio = 0.1
        for i in range(16):
            print(ratio)
            sound_resample = resample(sound_array, ratio, "sinc_fastest").astype(sound_array.dtype)
            out_sounds.append(pygame.sndarray.make_sound(sound_resample))
            ratio += 0.1
        module.sounds = out_sounds
