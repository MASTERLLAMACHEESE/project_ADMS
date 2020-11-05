#!/usr/bin/env python

import pygame
import time
import numpy

class Pitch:

    def __init__(self, btn):
        self.btn = btn
        self.sound_file = None
        self.snd_out = []

    def input(self, btn, type):
        if type == 'pitch ' and press_value == 1:
            change_back = True 
        elif type == 'pitch':
            press_value = 1
            self.set_pad()

    def resample(self, sound_file):
        self.sound_file = sound_file
        sound = pygame.mixer.Sound(self.sound_file)
        snd_array = pygame.sndarray.array(sound)
        for i in range(16):
            snd_resample = resample(snd_array, 1.5, "sinc_fastest").astype(snd_array.dtype)
            self.snd_out.append(pygame.sndarray.make_sound(snd_resample))

    def set_pad(self):
        self.snd_out