import pygame
import _thread
from sequencer import Sequencer
from pitch import Pitch

SOUND_LOCATION = './sounds'


class Controller:

    def __init__(self, bpm=124):
        self.bpm = bpm
        self.sounds = []
        pygame.mixer.init()
        for i in range(16):
            self.sounds.append(pygame.mixer.Sound(f"{SOUND_LOCATION}/{str(i+1)}.wav"))
        self.selected = None
        self.play_state = 0
        self.sequencer = Sequencer(self.bpm)
        self.pitch = Pitch()
        self.loop_thread = None

    def input(self, btn, type):
        if type == 'seq':
            self.seq_add(btn)
        if type == 'pad':
            self.seq_select(btn)
        if type == 'bpm':
            self.bpm_set(btn)
        if type == 'pitch':
            self.set_pitch(btn)

    def seq_select(self, btn):
        self.selected = btn
        self.sounds[self.selected].play()
        self.pitch.resample(self.sounds[self.selected])
        print(f'{self.selected} selected')

    def seq_add(self, btn):
        if self.selected:
            self.sequencer.add_sound(btn-1, self.sounds[self.selected])
            print(f'pad {self.selected} added to {btn}')
    
    def bpm_set(self, btn):
        print(f'{self.sequencer.bpm} old bpm')
        if btn == 1:
            if self.bpm < 190:
                self.bpm = self.bpm + 1
                self.sequencer.bpm = self.bpm
                print(f'{self.sequencer.bpm} current bpm')
        if btn == 2:
            if self.bpm > 60:
                self.bpm = self.bpm - 1
                self.sequencer.bpm = self.bpm
                print(f'{self.sequencer.bpm} current bpm')
        if btn == 3:
            self.bpm = 124
            self.sequencer.bpm = 124
            print(f'{self.sequencer.bpm} current bpm')

    def set_pitch(self, btn):
        self.pitch.btn = btn

        

    def seq_toggle_play(self):
        # Not working properly
        # if self.play_state == 1:
        #     self.loop_thread.exit()
        #     self.play_state = 0
        if self.play_state == 0:
            self.loop_thread = _thread.start_new_thread(self.sequencer, ())
            self.play_state = 1

    



    def mode_toggle(self):
        pass