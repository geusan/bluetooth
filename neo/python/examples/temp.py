# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *

import argparse
import signal
import sys
def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)

# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN2       = 22      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_CHANNEL2   = 0
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def program_exit(strip):
	for i in range(0, strip.numPixels()):
		strip.setPixelColor(i,Color(0,0,0))
        strip.setBrightness(0)
        strip.show()

def getMyColor(strip, n, _name):
        print(_name)
        if _name == 0:
                strip.setPixelColor(n, Color(255,0,0))
        elif _name == 1:
                strip.setPixelColor(n, Color(0,0,255))
        elif _name == 2:
                strip.setPixelColor(n, Color(0,255,0))
        else:
                strip.setPixelColor(n, Color(255,255,255))

        strip.show()
# Main program logic follows:
if __name__ == '__main__':
        # Process arguments
        opt_parse()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
#	strip2 = Adafruit_NeoPixel(LED_COUNT, LED_PIN2, LED_FREQ_HZ, LED_DMA,LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL2, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
        #strip2.begin()
	i=0
	print ('Press Ctrl-C to quit.')
        try:
                while True:
                        mycolor = int(input("get your color 0/1/2 "))
                        strip.setBrightness(255)
                        getMyColor(strip, i%8, mycolor)
#                        strip.setPixelColor(i%8,Color(255,0,0))
                        # strip.show()
                        i+=1
#                print(strip.getPixels(), strip.numPixels())
#                strip.setPixelColor(2,Color(255,255,255))
                
#                strip.setBrightness(255)
#                strip.show()
                #while True:
                #        for i in range(0, strip.numPixels(), 1):

                #               strip.setPixelColor(i,Color(255,255,255))
                        #colorWipe(strip, Color(255, 0, 0))

        		
        except KeyboardInterrupt:
        	print ('Exit program')
        	program_exit(strip)
                #program_exit(strip2)
