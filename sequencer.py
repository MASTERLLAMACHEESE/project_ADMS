import pygame
from datetime import datetime


class Sequencer:

    def __init__(self, bpm, loop=True):
        self.sounds_in_beat = [[None for x in range(4)] for y in range(16)]
        self.loop = loop
        self.delay = int((60 / bpm * 1000))
        print(self.delay)
        self.beat_counter = 0

    def __call__(self, *args, **kwargs):
        while self.loop is True:
            for i in range(16):
                for sound in self.sounds_in_beat[i]:
                    if sound is not None:
                        sound.play()
                pygame.time.delay(self.delay)
                if i == 15:
                    self.beat_counter = 0
                else:
                    self.beat_counter = i

    def add_sound(self, index, sound):
        if sound in self.sounds_in_beat[index]:
            self.sounds_in_beat[index].remove(sound)
        else:
            self.sounds_in_beat[index].append(sound)
