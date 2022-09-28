import RPi.GPIO as gpio
from time import sleep
from oop import *
from constants import ports_dac, ports_aux
from random import randint

gpio.setmode(gpio.BCM)

diods_dac = init_diods(ports_dac)
aux_pins = init_pins(ports_aux)


