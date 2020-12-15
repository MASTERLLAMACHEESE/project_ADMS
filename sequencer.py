import time
import module
import threading
from pydub.playback import play


def sequencer_loop():
    """
    This function starts in a separate thread.
    Plays sounds on every beat while sequencer is running
    """
    try:
        while module.seq_loop is True:
            for i in range(16):
                if not module.seq_loop:  # Checks if sequencer is working
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
                    # Starts new thread so that multiple sounds can play at the same time
                    threading.Thread(target=play, args=(mixed,)).start()
                # This is calculated so that sleep() delay would be as accurate as possible
                playtime = time.time() - prev
                time.sleep((module.delay - playtime) if playtime < module.delay else 0)
    except KeyboardInterrupt:
        return


class Sequencer:
    """
    Sequencer class for controlling sequencer playback
    """

    def __init__(self, start=False):
        """
        Sets default BPM and starts sequencer thread if start=True (default=False)
        """
        module.delay = (60 / module.bpm) / 2
        self.seq_thread = threading.Thread(target=sequencer_loop)
        if start:
            self.start()

    def start(self):
        """
        Starts sequencer in a separate thread
        """
        print(f'\n{module.current_time()} Starting sequencer\n'
              f'{module.current_time()} Please wait...')
        module.seq_loop = True
        time.sleep(1)
        self.seq_thread = threading.Thread(target=sequencer_loop)
        self.seq_thread.start()
        print(f'{module.current_time()} Sequencer ready\n')

    def stop(self):
        """
        Closes sequencer thread
        """
        print(f'\n{module.current_time()} Terminating sequencer\n'
              f'{module.current_time()} Please wait...')
        module.seq_loop = False
        self.seq_thread.join()  # Shuts down sequencer thread
        module.sounds_in_beat = [[] for y in range(16)]  # Clears sequencer from sounds
        print(f'{module.current_time()} Sequencer stopped\n')

    def toggle_play(self):
        """
        Either starts or stops sequencer. Depends on module.seq_loop value
        """
        if module.seq_loop:
            self.stop()
        else:
            self.start()
        print(f'{module.current_time()} Currently active threads: {threading.active_count()}')

    def toggle_sound(self, index, sound):
        """
        Inputs:
        index (int): beat position
        sound (sound object): sound object to add to beat

        Adds or removes sound from beat
        """
        if sound not in module.sounds_in_beat[index]:
            if len(module.sounds_in_beat[index]) < 4:
                module.sounds_in_beat[index].append(sound)
                print(f'{module.current_time()} SEQ: Added to pos: {index+1}')
            else:
                print(f'{module.current_time()} SEQ: Cannot add to pos: {index + 1}. Position is full')
        else:
            module.sounds_in_beat[index].remove(sound)
            print(f'{module.current_time()} SEQ: Removed from pos: {index+1}')
        time.sleep(0.3)

    def change_bpm(self, value):
        """
        Inputs:
        value (int): value to add to current BPM

        Changes sequencer BPM
        """
        if value == 124:  # Reset BPM to default value ToDo make this value changeable
            module.bpm = 124
        else:
            module.bpm += value

        module.delay = (60 / module.bpm) / 2
        print(f'{module.current_time()} Current bpm: {module.bpm}')