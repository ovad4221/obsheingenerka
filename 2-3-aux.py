import RPi.GPIO as gpio
from time import sleep
from oop import *
from constants import ports_dac, ports_aux

gpio.setmode(gpio.BCM)


diods_dac = init_diods(ports_dac)
aux_pins = init_pins(ports_aux, is_out=False)

time_sleep = 0.3
while True:
    binary = ""
    for pin in aux_pins:
        if pin.is_power():
            binary += '0'
        else:
            binary += '1'
    binary_to_leds(diods_dac, binary)
    sleep(time_sleep)
