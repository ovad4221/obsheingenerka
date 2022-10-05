from package.oop.oop import *
from package.constants import ports_dac, ports_aux


diods_dac = init_pins(ports_dac)
aux_pins = init_pins(ports_aux, is_out=False)

time_sleep = 0.3
while True:
    binary = ""
    # all_off(diods_dac)
    for pin in aux_pins:
        if pin.is_power():
            binary += '0'
        else:
            binary += '1'
    # binary = "10101010"
    binary_to_leds(diods_dac, binary)
    sleep(time_sleep)
