import RPi.GPIO as GPIO
import time
import json
import ast

from motor_tools import move_to
with open("image_code.txt", "r") as file:
    components = ast.literal_eval(file.read())

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


try:
    for component in components:
        print("NEW COMPONENT")
        for i in range(0, len(component)-1):
            print(component[i])
            pixel_x = int(component[i][0])
            pixel_y = int(component[i][1])
            move_to(pixel_x, pixel_y, int(component[i+1][0]),  int(component[i+1][1]))

except KeyboardInterrupt:
    GPIO.cleanup()
