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
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.


NUMPIXELS = 16  # Update this to match the number of LEDs.
BRIGHTNESS = 0.5  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.


def resetAll():
    for i in range(0, 16):
        pixels[i] = (10, 0, 0)  

def switchOnLed(led):
    pixels[led] = (100, 0, 0)   
    
def updateStrip(step):
    resetAll()
    switchOnLed(step)
    pixels.show()
    time.sleep(SPEED)


# MAIN

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

resetAll()

while True:
    for i in range(0, 16):
        updateStrip(i)    
    
    for i in range(15, -1, -1):
        updateStrip(i)    
