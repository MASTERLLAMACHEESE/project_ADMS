import settings
import pygame
from sequencer import Sequencer
from sound import Sound
from pitch import Pitch


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
        self.pitch = Pitch()
        self.loop_thread = None

    def input(self, btn_type, btn=None):
        if btn_type == 'seq':
            self.seq_add(btn)
        if btn_type == 'pad':
            self.seq_select(btn)
        # if btn_type == 'pad':
        #     self.seq_toggle_play()

    def seq_select(self, btn):
        self.selected = btn
        settings.sounds[self.selected].play()
        self.pitch.resample(settings[self.selected])
        print(f'{self.selected} selected')

    def seq_add(self, btn):
        if self.selected:
            self.sequencer.add_sound(btn-1, settings.sounds[self.selected].sound)
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