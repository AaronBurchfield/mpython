import neopixel
import machine
import time
import math
# Init rgbw pixel gema
np = neopixel.NeoPixel(machine.Pin(5), 7, 4)
frequency = 80


def lerp(x, x0, x1, y0, y1):
    return y0+(x-x0)*((y1-y0)/(x1-x0))


def get_color(tick):
    wave = math.sin(2.0*math.pi*frequency*tick)
    return int(lerp(wave, -1, 1, 0, 128))


def main():
    while True:
        tick = time.ticks_us()
        for i in range(7):
            color = get_color(tick)
            print(color)
            np[i] = (0, color, 0, 0)

        np.write()
        time.sleep(.1)


if __name__ == '__main__':
    main()
