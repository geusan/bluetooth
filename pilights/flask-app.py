import sys

from flask import Flask, request
from py import neopixels

DEBUG = True
NUM_LEDS = 8

app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

pixels = neopixels.new_instance(NUM_LEDS)


@app.route('/index')
def root():
    pixels.set_all(0,0,0)
    pixels.set_brightness(255)
    return app.send_static_file('index.html')


@app.route('/setcolor/<r>/<g>/<b>', methods=['GET'])
def set_color(r,g,b):
    r = int(r)
    g = int(g)
    b = int(b)
    pixels.set_all(r, g, b)
    return "OK"

@app.route('/setbrightness/<n>')
def set_brightness(n):
   n = int(n)
   pixels.set_brightness(n)
   return "OK"

@app.route('/setturn/<n>')
def setTurn(n):
   pixels.set_turn(int(n))
   return "OK"

@app.route('/mode/<mode>')
def set_mode(mode):
   if mode == "colorWipe":
       pixels.colorWipe(255,0,0)
       pixels.colorWipe(0,255,0)
       pixels.colorWipe(0,0,255)

   elif mode == "theaterChase":
       pixels.theaterChase(127,127,127)
       pixels.theaterChase(127,0,0)
       pixels.theaterChase(0,0,127)

   elif mode == "rainbow":
       # pixels.rainbow()
       pixels.rainbowCycle()
       # pixels.theaterChaseRainbow()

   pixels.set_all(0,0,0)
   return "OK %s" % mode

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
