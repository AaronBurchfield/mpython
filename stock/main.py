import neopixel
import machine
import json
import time
import urequests as requests


def get_quote(symbol):
    url = 'https://finance.google.com/finance/info?client=ig&q=%s' % symbol
    res = requests.get(url)
    js = json.loads(res.text[4:])
    return js[0]


def main():
    np = neopixel.NeoPixel(machine.Pin(5), 7, 4)
    symbols = ['AAPL', 'AMZN', 'GOOG', 'IBM', 'NVDA', 'TWTR', 'YELP']
    while True:
        np.fill((0, 0, 128, 0))
        np.write()
        for i in range(7):
            quote = get_quote(symbols[i])
            if '+' in str(quote['c']):
                color = (0, 128, 0, 0)
            else:
                color = (128, 0, 0, 0)

            np[i] = color
        np.write()
        time.sleep(5)


if __name__ == '__main__':
    main()
