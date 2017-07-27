# hacking around with micropython on esp8266-20170108

## installing micropython
1. download micropython image from https://micropython.org/download
2. find the serial port the board is on
  ```
  ls /dev/tty.*
  ```
3. erase existing flash
  ```
  esptool.py --port /dev/tty.wchusbserial14540 erase_flash
  ```
4. write micropython image
  ```
  esptool.py --port /dev/tty.wchusbserial14540 --baud 115200 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin
  ```

## esptool
serial bootloader for esp8266 boards
https://github.com/espressif/esptool

## ampy
interact with micropython board over serial
https://github.com/adafruit/ampy

1. tell ampy which interface to use
  ```
  export AMPY_PORT=/dev/tty.wchusbserial14440
  ```
2. update boot script
  ```
  ampy put boot.py
  ```
3. update main script
  ```
  ampy put main.py
  ```
