import time
import board
import module
import neopixel
import threading
pixels = neopixel.NeoPixel(board.D18, 60)
delay = 0.00001
pixels.fill((0, 0, 0))


# LED values (red, green, blue)
def leds():
    while True:
        pixels[module.seq_led] = (0, 255, 0) if module.seq_loop else (255, 0, 0)
        pixels[module.pitch_led] = (255, 128, 0) if module.pitch_mode else (0, 0, 0)
        pixels[module.playback_led] = (0, 255, 0) if module.playback else (255, 0, 0)
        time.sleep(0.01)


def start_led():
    threading.Thread(target=leds).start()
