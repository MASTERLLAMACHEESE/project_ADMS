"""
!!!This file only works on Raspberry Pi!!!
"""
import time
import board
import module
import neopixel
import threading
pixels = neopixel.NeoPixel(board.D18, 19)  # GPIO pin 18 is assigned to leds, 19 leds in total
pixels.fill((0, 0, 0))  # Initially turn all leds off
# LED values (red, green, blue), 0-255


def leds():
    """
    Shows status leds and shows sequencer beat position
    """
    while True:
        pixels[module.seq_led] = (0, 255, 0) if module.seq_loop else (255, 0, 0)
        pixels[module.pitch_led] = (255, 128, 0) if module.pitch_mode else (0, 0, 0)
        pixels[module.playback_led] = (0, 255, 0) if module.playback else (255, 0, 0)

        # shows sequencer position, if pad button pressed, temporarily hides sequencer progress
        if not module.pad_clicked and module.pos_in_seq == [] and module.seq_loop:
            for i, led in enumerate(module.seq_leds):
                pixels[led] = (255, 255, 255) if module.current_beat == i else (0, 0, 0)

        # seq leds turn off if sequencer is turned off
        if not module.seq_loop:
            for i, led in enumerate(module.seq_leds):
                pixels[led] = (0, 0, 0)
                module.current_beat = 0
        time.sleep(0.01)


def pos_in_seq():
    """
    Shows selected sound position on seq leds for 3 seconds
    """
    while True:
        if module.pad_clicked and not module.pos_in_seq == []:
            for i, led in enumerate(module.seq_leds):
                pixels[led] = (0, 0, 0)
            for pos in module.pos_in_seq:
                pixels[module.seq_leds[pos]] = (255, 0, 0)
            time.sleep(3)
        module.pad_clicked = False
        module.pos_in_seq = []
        time.sleep(0.1)


def start_led():
    """
    Start led threads
    ToDo These threads probably don't need to exist as threads, but there's no time to change that
    We could just make callback functions for them
    def change_seq_led(pos)
    def togglePitchLed() etc
    """
    threading.Thread(target=leds).start()
    threading.Thread(target=pos_in_seq).start()
