import time
import board
import module
import neopixel
import threading
pixels = neopixel.NeoPixel(board.D18, 19)
delay = 0.00001
pixels.fill((0, 0, 0))


# LED values (red, green, blue)
def leds():
    while True:
        pixels[module.seq_led] = (0, 255, 0) if module.seq_loop else (255, 0, 0)
        pixels[module.pitch_led] = (255, 128, 0) if module.pitch_mode else (0, 0, 0)
        pixels[module.playback_led] = (0, 255, 0) if module.playback else (255, 0, 0)
        if not module.pad_clicked:
            for i, led in enumerate(module.seq_leds):
                pixels[led] = (255, 255, 255) if module.current_beat == i else (0, 0, 0)
        time.sleep(0.01)


def pos_in_seq():
    while True:
        if module.pad_clicked:
            for pos in module.pos_in_seq:
                pixels[module.seq_leds[pos]] = (255, 0, 0)
            time.sleep(3)
            module.pad_clicked = False
            module.pos_in_seq = []
        time.sleep(0.1)


def start_led():
    threading.Thread(target=leds).start()
    threading.Thread(target=pos_in_seq).start()
