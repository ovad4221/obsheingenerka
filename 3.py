import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

while True:
    GPIO.output(14, GPIO.input(15))
    sleep(0.01)
