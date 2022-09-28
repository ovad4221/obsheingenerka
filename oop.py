import RPi.GPIO as gpio
from time import sleep


class Diod:
    def __init__(self, port):
        # print(port)
        self.port = port
        self.is_on = False
        gpio.setup(port, gpio.OUT)

    def on(self):
        gpio.output(self.port, 1)
        self.is_on = True
    
    def off(self):
        gpio.output(self.port, 0)
        self.is_on = False


def binary_to_leds(diods, binary):
    if 0 <= int(binary, 2) <= 255:
        for i in range(len(binary)):
            if binary[i] == '0':
                diods[i].off()
            else:
                diods[i].on()
        return True
    else:
        print('Incorrect int')
        return False


# simple running
def run_zm(diods, step):
    diods[0].on()
    sleep(step)
    for i in range(1, 8):
        diods[i].on()
        diods[i - 1].off()
        sleep(step)
    diods[-1].off()


def all_off(diods):
    for diod in diods:
        diod.off()
