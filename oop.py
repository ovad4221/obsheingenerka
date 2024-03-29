import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)


class Pin:
    def __init__(self, port, is_out=True):
        # print(port)
        self.port = port
        self.is_out = is_out
        if is_out:
            gpio.setup(port, gpio.OUT)
        else:
            gpio.setup(port, gpio.IN)

    def is_power(self):
        if self.is_out:
            return 'pin init as out'
        if not gpio.input(self.port):
            # if power is on
            return True
        else:
            return False


class Diod(Pin):
    def __init__(self, port, is_out=True):
        super().__init__(port)
        self.is_on = False

    def on(self):
        gpio.output(self.port, 1)
        self.is_on = True

    def off(self):
        gpio.output(self.port, 0)
        self.is_on = False


def init_pins(ports, class_of=Pin, is_out=True):
    pins = []
    for i in range(len(ports)):
        pins.append(class_of(ports[i], is_out=is_out))
    return pins


def init_diods(ports):
    return init_pins(ports, class_of=Diod)


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
