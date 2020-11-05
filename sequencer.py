import settings
import pygame
import threading


def sequencer_loop():
    while settings.loop is True:
        if settings.stop_sequencer:
            break
        for i in range(16):
            for sound in settings.sounds_in_beat[i]:
                if sound is not None:
                    sound.play()
            pygame.time.delay(settings.delay)


class Sequencer:

    def __init__(self, start=False):
        self.seq_thread = threading.Thread(target=sequencer_loop, args=())
        if start:
            self.start()

    def start(self):
        settings.stop_thread = False
        print(f'Sequencer started')
        self.seq_thread.start()

    def stop(self):
        settings.stop_thread = True

    def add_sound(self, index, sound):
        if sound in settings.sounds_in_beat[index]:
            settings.sounds_in_beat[index].remove(sound)
        else:
            settings.sounds_in_beat[index].append(sound)
