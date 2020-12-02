import time
import module
import threading


def sequencer_loop():
    try:
        while module.seq_loop is True:
            for i in range(16):
                if not module.seq_loop:
                    break
                module.current_beat = i
                prev = time.time()
                sounds = module.sounds_in_beat[i]
                mixed = None
                if len(sounds) == 4:
                    mixed = sounds[0].overlay(sounds[1]).overlay(sounds[2]).overlay(sounds[3])
                if len(sounds) == 3:
                    mixed = sounds[0].overlay(sounds[1]).overlay(sounds[2])
                if len(sounds) == 2:
                    mixed = sounds[0].overlay(sounds[1])
                if len(sounds) == 1:
                    mixed = sounds[0]
                if mixed:
                    module.blink_led = True
                    threading.Thread(target=play, args=(mixed,)).start()
                playtime = time.time() - prev
                time.sleep((module.delay - playtime) if playtime < module.delay else 0)
    except KeyboardInterrupt:
        return


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
        if sound not in module.sounds_in_beat[index]:
            module.sounds_in_beat[index].append(sound)
            print(f'{module.current_time()} SEQ: Added to pos: {index+1}')
        else:
            module.sounds_in_beat[index].remove(sound)
            print(f'{module.current_time()} SEQ: Removed from pos: {index+1}')
        time.sleep(0.3)

    def change_bpm(self, value):
        if value == 124:
            module.bpm = 124
        else:
            module.bpm += value

        module.delay = (60 / module.bpm) / 2
        print(f'{module.current_time()} Current bpm: {module.bpm}')