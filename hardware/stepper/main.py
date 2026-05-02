import RPi.GPIO as GPIO
import time

PUL = 18
DIR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)

GPIO.output(DIR, GPIO.HIGH)

try:
    while True:
        GPIO.output(PUL, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(PUL, GPIO.LOW)
        time.sleep(0.001)

except KeyboardInterrupt:
    GPIO.cleanup()
