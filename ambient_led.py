import time
import board
import module
import neopixel
import threading
pixels = neopixel.NeoPixel(board.D18, 60)
delay = 0.00001
pixels.fill((0, 0, 0))


# LED values (red, green, blue)
def ambient():
    while True:
        if module.blink_led:
            for i in range(30):
                pixels[i+30] = (255, 0, 255)

            for i in range(30):
                pixels[i+30] = (0, 0, 0)
            module.blink_led = False
        time.sleep(0.01)


def start_ambient():
    threading.Thread(target=ambient).start()
