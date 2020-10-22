import pygame
import _thread
from looper import Looper


class Controller:

    def __init__(self, bpm=127):
        self.bpm = bpm
        self.sounds = []
        pygame.mixer.pre_init(44100, 16, 1, 4096)
        pygame.mixer.init()
        for i in range(16):
            self.sounds.append(pygame.mixer.Sound(f"/media/usb/{str(i+1)}.wav"))
        self.selected = None
        self.play_state = 0
        self.looper = Looper(self.bpm)
        self.loop_thread = None

    def select(self, btn):
        self.selected = btn
        print(f'{self.selected} selected')

    def add(self, btn):
        if self.selected:
            self.looper.add_sound(btn-1, self.sounds[self.selected])
            print(f'pad {self.selected} added to {btn}')

    def toggle_play(self):
        # Not working properly
        # if self.play_state == 1:
        #     self.loop_thread.exit()
        #     self.play_state = 0
        if self.play_state == 0:
            self.loop_thread = _thread.start_new_thread(self.looper, ())
            self.play_state = 1
