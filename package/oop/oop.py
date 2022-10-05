import RPi.GPIO as gpio
from time import sleep
from package.constants import *

gpio.setmode(gpio.BCM)


class Pin:
    def __init__(self, port):
        self.port = port


class Pin_In(Pin):
    def __init__(self, port):
        super().__init__(port)
        gpio.setup(port, gpio.IN)

    def is_power(self):
        if not gpio.input(self.port):
            # if power is on
            return True
        else:
            return False


class Pin_Out(Pin):
    def __init__(self, port):
        super().__init__(port)
        gpio.setup(port, gpio.OUT)
        self.is_on = False

    def on(self):
        gpio.output(self.port, 1)
        self.is_on = True

    def off(self):
        gpio.output(self.port, 0)
        self.is_on = False

    # false reliase
    def shim_perc(self, perc=1, report=False):
        if perc < 0:
            perc = 0
            print("voltage percentage must be > 0 and < 1, taked 0%")
        elif perc > 1:
            perc = 1
            print("voltage percentage must be > 0 and < 1, taked 100%")
        gpio.output(self.port, bin(int(255 * perc))[2:].zfill(8))
        if report:
            volts = 3.3 * perc
            print(f"To {self.port} port filed {3.3 * perc}V")


def init_pins(ports, is_out=True):
    pins = []
    if is_out:
        class_of = Pin_Out
    else:
        class_of = Pin_In
    for i in range(len(ports)):
        pins.append(class_of(ports[i]))
    return pins


def binary_to_leds(diods, binary, lights=1, report=False):
    if 0 <= int(binary, 2) <= 255:
        if report:
            print(f"To leds field {int(binary, 2) / 256 * 3.3}V")

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
def run_zm(diods, step, light=1):
    diods[0].off()
    sleep(step)
    for i in range(1, 8):
        diods[i].on()
        diods[i - 1].off()
        sleep(step)
    diods[-1].on()


def all_off(how='all'):
    if how == 'all':
        gpio.cleanup()
    elif how == 'ld_pins':
        for pin in ports_dac + ports_leds:
            pin.off()
