import machine
import time
import json
import neopixel
import urequests as requests

url = 'http://10.0.0.88:5000'
np = neopixel.NeoPixel(machine.Pin(5), 7, 4)


def get_status():
    res = requests.get(url)
    js = json.loads(res.text)
    color = js.get('color', None)
    pattern = js.get('pattern', None)
    return color, pattern


def main():
    while True:
        # np[0] = (0, 0, 64, 0)
        # np.write()
        color, pattern = get_status()
        if pattern == 'solid':
            fill_color = color
        else:
            fill_color = (128, 0, 0, 0)

        np.fill(fill_color)
        np.write()
        # time.sleep(2)
        # np.fill((0, 0, 0, 0))
        # np.write()
        time.sleep(1)


if __name__ == '__main__':
    main()
