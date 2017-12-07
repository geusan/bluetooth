from flask import Flask, render_template

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
        signal.signal(signal.SIGNT, signal_handler)


LED_COUNT   = 8
LED_PIN     = 13
LED_FREQ_HZ = 800000
LED_DMA     = 5
LED_BRIGHTNESS = 255
LED_INVERT  = False
LED_CHANNEL = 1
LED_STRIP   = ws.WS2811_STRIP_GRB

app = Flask(__name__)

# opt_parse()

strip = None
# strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
#strip.begin()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/all/<color>')
def all(color):
    global strip
    cc = Color(0,0,0)
    if color == "red":
        cc = Color(255,0,0)
    elif color == "blue":
        cc = Color(0,0,255)
    else:
        cc = Color(255,255,255)
    
    if strip == None:
        strip = init()
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i,cc)

    strip.show()
    return render_template('home.html')



def init(): 
    global LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()
    return strip

if __name__ == '__main__':
    app.run(host='192.168.1.10', port=80, debug=True)
    opt_parse()
    
    
#    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
#strip.begin()
#    strip.begin()

#    print('Press Ctrl-C to quit')

#    try:
#        while True:
#            print ('color wipe animation')
            
#    except KeyboardInterrupt:
#       strip.setBrightness(0)
#       strip.show()
#       print('program quit')
