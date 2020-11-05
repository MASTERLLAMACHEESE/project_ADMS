import settings
import pygame
from sequencer import Sequencer
from sound import Sound


class Controller:

    def __init__(self):
        pygame.mixer.init()
        for i in range(16):
            sound = Sound(f"{settings.sound_location}/{str(i+1)}.wav")
            sound.pad_pos = i
            settings.sounds.append(sound)
        self.selected = None
        self.play_state = 0
        self.sequencer = Sequencer(start=True)
        self.loop_thread = None

    def input(self, btn_type, btn=None):
        if btn_type == 'seq':
            self.seq_add(btn)
        if btn_type == 'pad':
            self.seq_select(btn)
        if btn_type == 'bpm':
            self.bpm_set(btn)

    def seq_select(self, btn):
        self.selected = btn
        settings.sounds[self.selected].play()
        print(f'{self.selected} selected')

    def seq_add(self, btn):
        if self.selected:
            self.sequencer.add_sound(btn-1, settings.sounds[self.selected].sound)
            print(f'pad {self.selected} added to {btn}')
    
    def bpm_set(self, btn):
        if btn == 1:
            if settings.bpm < 190:
                settings.bpm = settings.bpm + 1
                print(f'{settings.bpm} current bpm')
        if btn == 2:
            if settings.bpm > 60:
                settings.bpm = settings.bpm - 1
                print(f'{settings.bpm} current bpm')
        if btn == 3:
            settings.bpm = 124
            print(f'{settings.bpm} current bpm')
        settings.delay = int((60 / settings.bpm * 1000))

    # def seq_toggle_play(self):
        # Not working properly
        # if self.play_state == 1:
        #     self.sequencer.stop()
        #     self.play_state = 0
        # if self.play_state == 0:
        #     self.sequencer.start()
        #     self.play_state = 1

    def mode_toggle(self):
        pass