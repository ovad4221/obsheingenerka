from package.oop.oop import *
from package.constants import *
import csv
import time
from math import floor

dac = init_pins(ports_dac)
leds = init_pins(ports_leds)
comp = Pin_In(4)
troyka = Pin_Out(17)


# return % in the form of a fraction
def voltage():
    # 0 1 0 1 1 1 1 0
    binary = [1, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        binary_to_leds(dac, ''.join([str(i) for i in binary]))
        time.sleep(0.0001)
        # comp.i_p True when V dac > V adc
        if i != 7:
            if comp.is_power():
                binary[i], binary[i + 1] = 0, 1
            else:
                binary[i], binary[i + 1] = 1, 1
        else:
            if comp.is_power():
                binary[i] = 0
            else:
                binary[i] = 1

    st_one = '1' * floor(int(''.join([str(i) for i in binary]), 2) / 245 * 8)
    binary_to_leds(leds, st_one.zfill(8))
    return int(''.join([str(i) for i in binary]), 2) / 256 * 3.3


try:
    with open('data_RC.csv', 'w') as file:
        troyka.on()
        file.write('t,Volt')
        v_old = 0.0
        time1 = time.time_ns()
        while True:
            v_new = voltage()
            file.write(f"{time.time_ns() - time1},{round(v_new, 5)}\n")
            if abs(v_new - v_old) < 0.01:
                if troyka.is_on:
                    troyka.off()
                else:
                    troyka.on()
            v_old = v_new
            sleep(0.01)
finally:
    all_off()
