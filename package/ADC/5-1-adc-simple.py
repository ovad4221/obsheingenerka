from package.oop.oop import *
from package.constants import *
from time import sleep

dac = init_pins(ports_dac)
comp = Pin_In(4)
troyka = Pin_Out(17, initial=True)

try:
    while True:
        for i in range(256):
            binary_to_leds(dac, bin(i)[2:])
            if comp.is_power():
                print(f"ADC step = {i}; voltage DAC = {i / 256 * 3.3} V")
                break
            sleep(0.001)

except Exception as error:
    print(str(error))
finally:
    all_off()
