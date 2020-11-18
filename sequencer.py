import time
import module
import threading
from pydub.playback import play


def sequencer_loop():
    while module.seq_loop is True:
        for i in range(16):
            prev = time.time()
            mixer = None
            for sound in module.sounds_in_beat[i]:
                if not mixer:
                    mixer = sound
                else:
                    mixer = mixer.overlay(sound)
            if mixer:
                play(mixer)
            sys_delay = time.time() - prev
            time.sleep(module.delay-(sys_delay if sys_delay != 0 else module.delay))


class Sequencer:

    def __init__(self, start=False):
        module.delay = 60 / module.bpm
        self.seq_thread = threading.Thread(target=sequencer_loop)
        if start:
            self.start()

    def start(self):
        print(f'\n{module.current_time()} Starting sequencer\n'
              f'{module.current_time()} Please wait...')
        module.seq_loop = True
        time.sleep(1)
        self.seq_thread = threading.Thread(target=sequencer_loop)
        self.seq_thread.start()
        print(f'{module.current_time()} Sequencer ready\n')

    def stop(self):
        print(f'\n{module.current_time()} Terminating sequencer\n'
              f'{module.current_time()} Please wait...')
        module.seq_loop = False
        self.seq_thread.join()
        module.sounds_in_beat = [[] for y in range(16)]
        print(f'{module.current_time()} Sequencer stopped\n')

    def toggle_play(self):
        if module.seq_loop:
            self.stop()
        else:
            self.start()
        print(f'{module.current_time()} Currently active threads: {threading.active_count()}')

    def toggle_sound(self, index, sound):
        if sound in module.sounds_in_beat[index]:
            module.sounds_in_beat[index].remove(sound)
        else:
            module.sounds_in_beat[index].append(sound)

    def change_bpm(self, value):
        if value == 124:
            module.bpm = 124
        else:
            module.bpm += value

        module.delay = (60 / module.bpm) / 2
        print(f'{module.current_time()} Current bpm: {module.bpm}')
