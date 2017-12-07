import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print "Setup LED pins as outputs"

GPIO.setup(26, GPIO.OUT)
GPIO.output(26, False)
GPIO.setup(19,GPIO.IN)


try: 
    # GPIO.output(26, False)
    print "Press the button (CTRL-C to exit)"

    while True:

        # GPIO.output(26, False)
        print GPIO.input(19)

        if GPIO.input(19)==0:
            print "Button Pressed"
            GPIO.output(26, True)
        else:
            print "Button Unpressed"
            GPIO.output(26, False)
        
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
