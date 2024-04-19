# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel


# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
PIN = board.D18 

# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18
SPEED = 0.2  # Increase to slow down the rainbow. Decrease to speed it up.


NUMPIXELS = 16  # Update this to match the number of LEDs.
BRIGHTNESS = 0.5  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

while True:
    for pixel in range(len(pixels)):
        pixels[pixel] = (0, 0, 0) # LED 1
    pixels[0] = (10, 0, 0) # LED 1
    pixels.show()
    time.sleep(SPEED)

    pixels[0] = (0, 0, 0) # LED 1
    pixels[1] = (10, 0, 0) # LED 2
    pixels.show()
    time.sleep(SPEED)

    
    pixels[1] = (0, 0, 0) # LED 2
    pixels[2] = (10, 0, 0) # LED 3
    pixels.show()
    time.sleep(SPEED)

    pixels[2] = (0, 0, 0) # LED 3
    pixels[3] = (10, 0, 0) # LED 4
    pixels.show()
    time.sleep(SPEED)

    pixels[3] = (0, 0, 0) # LED 4
    pixels[4] = (10, 0, 0) # LED 5
    pixels.show()
    time.sleep(SPEED)

    pixels[4] = (0, 0, 0) # LED 5
    pixels[5] = (10, 0, 0) # LED 6
    pixels.show()
    time.sleep(SPEED)

    pixels[5] = (0, 0, 0) # LED 6
    pixels[6] = (10, 0, 0) # LED 7
    pixels.show()
    time.sleep(SPEED)

    pixels[6] = (0, 0, 0) # LED 7
    pixels[7] = (10, 0, 0) # LED 8
    pixels.show()
    time.sleep(SPEED)

    pixels[7] = (0, 0, 0) # LED 8
    pixels[8] = (10, 0, 0) # LED 9
    pixels.show()
    time.sleep(SPEED)

    pixels[8] = (0, 0, 0) # LED 9
    pixels[9] = (10, 0, 0) # LED 10
    pixels.show()
    time.sleep(SPEED)

    pixels[9] = (0, 0, 0) # LED 10
    pixels[10] = (10, 0, 0) # LED 11
    pixels.show()
    time.sleep(SPEED)

    pixels[10] = (0, 0, 0) # LED 11
    pixels[11] = (10, 0, 0) # LED 12
    pixels.show()
    time.sleep(SPEED)

    pixels[11] = (0, 0, 0) # LED 12
    pixels[12] = (10, 0, 0) # LED 13
    pixels.show()
    time.sleep(SPEED)

    pixels[12] = (0, 0, 0) # LED 13
    pixels[13] = (10, 0, 0) # LED 14
    pixels.show()
    time.sleep(SPEED)

    pixels[13] = (0, 0, 0) # LED 14
    pixels[14] = (10, 0, 0) # LED 15
    pixels.show()
    time.sleep(SPEED)

    pixels[14] = (0, 0, 0) # LED 15
    pixels[15] = (10, 0, 0) # LED 16
    pixels.show()
    time.sleep(SPEED)

    pixels[14] = (10, 0, 0) # LED 15
    pixels[15] = (0, 0, 0) # LED 16
    pixels.show()
    time.sleep(SPEED)

    pixels[13] = (10, 0, 0) # LED 14
    pixels[14] = (0, 0, 0) # LED 15
    pixels.show()
    time.sleep(SPEED)

    pixels[12] = (10, 0, 0) # LED 13
    pixels[13] = (0, 0, 0) # LED 14
    pixels.show()
    time.sleep(SPEED)

    pixels[11] = (10, 0, 0) # LED 12
    pixels[12] = (0, 0, 0) # LED 13
    pixels.show()
    time.sleep(SPEED)

    pixels[10] = (10, 0, 0) # LED 11
    pixels[11] = (0, 0, 0) # LED 12
    pixels.show()
    time.sleep(SPEED)

    pixels[9] = (10, 0, 0) # LED 10
    pixels[10] = (0, 0, 0) # LED 11
    pixels.show()
    time.sleep(SPEED)

    pixels[8] = (10, 0, 0) # LED 9
    pixels[9] = (0, 0, 0) # LED 10
    pixels.show()
    time.sleep(SPEED)

    pixels[7] = (10, 0, 0) # LED 8
    pixels[8] = (0, 0, 0) # LED 9
    pixels.show()
    time.sleep(SPEED)

    pixels[6] = (10, 0, 0) # LED 7
    pixels[7] = (0, 0, 0) # LED 8
    pixels.show()
    time.sleep(SPEED)

    pixels[5] = (10, 0, 0) # LED 6
    pixels[6] = (0, 0, 0) # LED 7
    pixels.show()
    time.sleep(SPEED)

    pixels[4] = (10, 0, 0) # LED 5
    pixels[5] = (0, 0, 0) # LED 6
    pixels.show()
    time.sleep(SPEED)

    pixels[3] = (10, 0, 0) # LED 4
    pixels[4] = (0, 0, 0) # LED 5
    pixels.show()
    time.sleep(SPEED)

    pixels[2] = (10, 0, 0) # LED 3
    pixels[3] = (0, 0, 0) # LED 4
    pixels.show()
    time.sleep(SPEED)

    pixels[1] = (10, 0, 0) # LED 2
    pixels[2] = (0, 0, 0) # LED 3
    pixels.show()
    time.sleep(SPEED)

    pixels[0] = (10, 0, 0) # LED 1
    pixels[1] = (0, 0, 0) # LED 2
    pixels.show()
    time.sleep(SPEED)