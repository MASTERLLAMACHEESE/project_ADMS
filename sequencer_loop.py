import time
import module
from pydub.playback import play


def sequencer_loop():
    module.sounds_in_beat = [
    [module.sounds[0], module.sounds[5], module.sounds[7]],
    [module.sounds[0], module.sounds[7]],
    [module.sounds[0], module.sounds[5], module.sounds[7]],
    [module.sounds[0], module.sounds[7]],
    [module.sounds[0], module.sounds[5], module.sounds[7]],
    [module.sounds[0], module.sounds[7]],
    [module.sounds[0], module.sounds[5], module.sounds[7]],
    [module.sounds[0], module.sounds[7]],
    [module.sounds[0], module.sounds[5], module.sounds[7]],
    [module.sounds[0], module.sounds[7]],
    [module.sounds[0], module.sounds[5], module.sounds[7]],
    [module.sounds[0], module.sounds[7]],
    [module.sounds[0], module.sounds[5], module.sounds[7]],
    [module.sounds[0], module.sounds[7]],
    [module.sounds[0], module.sounds[5], module.sounds[7]],
    [module.sounds[0], module.sounds[7]],

]
    while module.seq_loop is True:
        for i in range(16):
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
                play(mixed)

            sys_delay = time.time() - prev
            time.sleep(module.delay - (sys_delay if sys_delay < module.delay else module.delay))