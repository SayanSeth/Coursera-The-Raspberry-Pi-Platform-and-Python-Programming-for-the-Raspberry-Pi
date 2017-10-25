# Build a circuit using your Raspberry Pi that causes an
# LED to blink when a push button is NOT pressed.
# However, the LED should stay on continuously when the push button IS pressed.


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledPin = 18
buttonPin = 17

GPIO.setup(ledPin, GPIO.OUT)  # LED pin set as output
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button pin set as input w/ pull-up

while True:
    try:
        if GPIO.input(buttonPin):   # when button is not Pressed
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(1)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(1)
        else:   # when button is Pressed
            GPIO.output(ledPin, GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()  # cleanup all GPIO
        print("\n Stopped")
        exit()
