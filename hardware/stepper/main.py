import RPi.GPIO as GPIO
import time

with open("image_code.txt", "r") as file:
    components = file.read()

print(components)

PULX = 18
DIRX = 23

PULY = 24
DIRY = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(PULX, GPIO.OUT)
GPIO.setup(DIRX, GPIO.OUT)
GPIO.setup(PULY, GPIO.OUT)
GPIO.setup(DIRY, GPIO.OUT)

GPIO.output(DIRX, GPIO.HIGH)
GPIO.output(DIRX, GPIO.LOW)

try:
    while True:
        GPIO.output(PULX, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(PULX, GPIO.LOW)
        time.sleep(0.001)

except KeyboardInterrupt:
    GPIO.cleanup()
