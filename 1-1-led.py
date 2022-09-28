import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

n = 0
while n != 1000:
    print(1)
    if n % 2:
        print(3)
        GPIO.output(14, 1)
    else:
        print(2)
        GPIO.output(14, 0)
    sleep(2)
    n += 1
