## RGB K2000
This project demonstrates manipulation of LEDs using a raspberry PI 3B+ an Intelligent IC addressable LED strip (WS2812B 5050 RGBIC)

Programs:

-   pixel.py: Flash LEDs repeatedly with rainbow colors
-   simple.py: Flash LEDs in the same pattern as the K2000 car
-   simple_2.py: A better version of k2000_long.py


### Dependencies
[Adafruit CircuitPython](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/tree/main)

### Quick start


```bash
$ git clone git@github.com:D-TOR11/rgb-k2000.git
$ cd rgb-command
$ sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
```

### Running command

```bash
$ sudo python3 pixel.py
```
