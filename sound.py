import pygame


class Sound:

    def __init__(self, filepath=None):
        self.sound = None
        if filepath:
            self.sound = pygame.mixer.Sound(f"{filepath}")
        self.name = filepath
        self.pad_pos = None
        self.seq_pos = None

    def play(self):
        if self.sound:
            self.sound.play()
