import time
import module
import threading


def sequencer_loop():
    while module.seq_loop is True:
        for i in range(16):
            for sound in module.sounds_in_beat[i]:
                if sound is not None:
                    sound.play()
            time.sleep(module.delay)


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
        print(f'Currently active threads: {threading.active_count()}')

    def toggle_sound(self, index, sound):
        if sound in module.sounds_in_beat[index]:
            module.sounds_in_beat[index].remove(sound)
        else:
            if len(module.sounds_in_beat[index]) < 4:
                module.sounds_in_beat[index].append(sound)

    def change_bpm(self, value):
        if value == 124:
            module.bpm = 124
        else:
            module.bpm += value
        module.delay = 60 / module.bpm
