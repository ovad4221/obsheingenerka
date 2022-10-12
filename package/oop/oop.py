import RPi.GPIO as gpio
from time import sleep
from package.constants import *

gpio.setmode(gpio.BCM)


class Pin:
    def __init__(self, port):
        self.port = port


class Pin_In(Pin):
    def __init__(self, port, report=False):
        super().__init__(port)
        gpio.setup(port, gpio.IN)
        self.report = report

    def is_power(self):
        if not gpio.input(self.port):
            # if power is on
            return True
        else:
            return False


class Pin_Out(Pin):
    def __init__(self, port, start_freq=1000, report=False):
        super().__init__(port)
        gpio.setup(port, gpio.OUT)
        self.is_on = False
        self.pwm = gpio.PWM(port, start_freq)
        self.report = report

    def on(self):
        gpio.output(self.port, 1)
        self.is_on = True
        if self.report:
            print(f"Pin {self.port} is on")

    def off(self):
        gpio.output(self.port, 0)
        self.is_on = False
        if self.report:
            print(f"Pin {self.port} is off")

    def start_pwm(self, dc):
        self.pwm.start(dc)
        if self.report:
            print(f"PWM in port {self.port} is started")

    def stop_pwm(self):
        self.pwm.stop()
        if self.report:
            print(f"PWM in port {self.port} is stopped")

    def change_dc(self, new_dc):
        self.pwm.ChangeDutyCycle(new_dc)
        if self.report:
            print(f"PWM duty cycle in port {self.port} is changed to {new_dc}")

    def change_freq(self, new_freq):
        self.pwm.ChangeFrequency(new_freq)
        if self.report:
            print(f"PWM frequency in port {self.port} is changed to {new_freq} Hz")


def init_pins(ports, is_out=True, report=False):
    pins = []
    if is_out:
        class_of = Pin_Out
    else:
        class_of = Pin_In
    for i in range(len(ports)):
        pins.append(class_of(ports[i], report=report))
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


def all_off(how='all', pins=None):
    if how == 'all':
        gpio.cleanup()
    elif how == 'ld_pins':
        if pins:
            for pin in pins:
                pin.off()
        else:
            print("Can't off. Pass a list of Pins to the function, please.")
    else:
        print("What do you want to set off?")
