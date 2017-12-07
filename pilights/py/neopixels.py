from __future__ import print_function

try:
    from neopixel import *

    mock = False
except ImportError:
    print("No neopixel library found - will generate mock NeoPixels objects")
    mock = True


def new_instance(num_leds):
    if mock:
        return NeoPixelsMock(num_leds)
    else:
        return NeoPixels(num_leds)


class NeoPixels:

    def __init__(self, num_leds, output_pin=18, led_freq_hz=800000, dma=5,
                 invert=False, brightness=255, channel=0, strip=ws.WS2811_STRIP_GRB):
        self.pixels = Adafruit_NeoPixel(num_leds, output_pin, led_freq_hz, dma,invert, brightness, channel, strip)
        self.pixels.begin()
        print("make neopixels")

    def set_all(self, r, g, b):
        """ Set all pixels to the given color """
        print("do set_all",r,g,b)
        col = Color(r, g, b)
        for i in range(self.pixels.numPixels()):
            self.pixels.setPixelColor(i, col)
        self.pixels.show()

    def set_pixel(self, n, r, g, b):
        col = Color(r, g, b)
        self.pixels.setPixelColor(n, col)
        self.pixels.show()

    def set_brightness(self, brightness):
        self.pixels.setBrightness(brightness)
        self.pixels.show()

    def colorWipe(self, r,g,b, wait_ms=50):
    	"""Wipe color across display a pixel at a time."""
        col = Color(r,g,b)
    	for i in range(strip.numPixels()):
    		self.pixels.setPixelColor(i, col)
    		self.pixels.show()
    		time.sleep(wait_ms/1000.0)

    def wheel(self, pos):
    	"""Generate rainbow colors across 0-255 positions."""
    	if pos < 85:
    		return Color(pos * 3, 255 - pos * 3, 0)
    	elif pos < 170:
    		pos -= 85
    		return Color(255 - pos * 3, 0, pos * 3)
    	else:
    		pos -= 170
    		return Color(0, pos * 3, 255 - pos * 3)

    def theaterChase(self, r,g,b , wait_ms=50, iterations=10):
    	"""Movie theater light style chaser animation."""
        col = Color(r,g,b)
    	for j in range(iterations):
    		for q in range(3):
    			for i in range(0, self.pixels.numPixels(), 3):
    				self.pixels.setPixelColor(i+q, col)
    			self.pixels.show()
    			time.sleep(wait_ms/1000.0)
    			for i in range(0, self.pixels.numPixels(), 3):
    				self.pixels.setPixelColor(i+q, 0)

    def rainbow(self, wait_ms=20, iterations=1):
    	"""Draw rainbow that fades across all pixels at once."""
    	for j in range(256*iterations):
    		for i in range(self.pixels.numPixels()):
    			self.pixels.setPixelColor(i, wheel((i+j) & 255))
    		self.pixels.show()
    		time.sleep(wait_ms/1000.0)

    def rainbowCycle(self, wait_ms=20, iterations=5):
    	"""Draw rainbow that uniformly distributes itself across all pixels."""
    	for j in range(256*iterations):
    		for i in range(self.pixels.numPixels()):
    			self.pixels.setPixelColor(i, wheel((int(i * 256 / self.pixels.numPixels()) + j) & 255))
    		self.pixels.show()
    		time.sleep(wait_ms/1000.0)

    def theaterChaseRainbow(self, wait_ms=50):
    	"""Rainbow movie theater light style chaser animation."""
    	for j in range(256):
    		for q in range(3):
    			for i in range(0, self.pixels.numPixels(), 3):
    				self.pixels.setPixelColor(i+q, wheel((i+j) % 255))
    			self.pixels.show()
    			time.sleep(wait_ms/1000.0)
    			for i in range(0, self.pixels.numPixels(), 3):
    				self.pixels.setPixelColor(i+q, 0)

class NeoPixelsMock:

    def __init__(self, num_leds, output_pin=18, led_freq_hz=800000, dma=5,
                 invert=False, brightness=255):
        pass

    def set_all(self, r, g, b):
        print("Set all to ", r, g, b)
