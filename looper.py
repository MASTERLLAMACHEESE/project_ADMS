import pygame


class Looper:

    def __init__(self, bpm, loop=True):
        self.sounds_in_beat = [[None for x in range(4)] for y in range(16)]
        self.loop = loop
        self.bpm = bpm
        self.beat_counter = 0

        pygame.mixer.pre_init(44100, 16, 1, 4096)
        pygame.mixer.init()

    def add_sound(self, sound):
        self.sounds_in_beat[self.beat_counter].append(sound)

    def loop(self):
        while self.loop is True:
            for i in range(16):
                for sound in self.sounds_in_beat[i]:
                    if sound is not None:
                        sound.play()
                print(f'on loop {i}')
                pygame.time.delay(float(60 / self.bpm * 1000))
                if i == 15:
                    self.beat_counter = 0
                else:
                    self.beat_counter = i
