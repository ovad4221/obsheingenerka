from package.oop.oop import *
from package.constants import *
from time import sleep

dac = init_pins(ports_dac)
comp = Pin_In(4)
troyka = Pin_Out(17, initial=True)

try:
    while True:
        i = int(input())
        binary_to_leds(dac, bin(i)[2:].zfill(8))
        print(f"voltage DAC = {i / 256 * 3.3} V")

except Exception as error:
    print(str(error))
finally:
    all_off()
