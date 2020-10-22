import pygame
import _thread
from .looper import Looper


class Controller:

    def __init__(self, bpm=127):
        self.bpm = bpm
        self.sounds = []
        for i in range(16):
            self.sounds.append(pygame.mixer.Sound(f"/media/usb/{str(i+1)}.wav"))

        self.looper = Looper(self.bpm)
        _thread.start_new_thread(self.looper.loop(), ())

    def execute(self, btn):
        self.looper.add_sound(self.sounds[btn-1])


