import sys

from flask import Flask, request
from py import neopixels

DEBUG = True
NUM_LEDS = 8

app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

pixels = neopixels.new_instance(NUM_LEDS)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/setcolor/<r>/<g>/<b>', methods=['GET'])
def set_color(r,g,b):
    r = int(r)
    g = int(g)
    b = int(b)
    pixels.set_all(r, g, b)
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
