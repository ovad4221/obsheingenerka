from package.oop.oop import *
from package.constants import *
from time import sleep

dac = init_pins(ports_dac)
comp = Pin_In(4)
troyka = Pin_Out(17, initial=True)

try:
    while True:
        binary = '10000000'
        for i in range(8):
            binary_to_leds(dac, binary)
            # comp.i_p True when V dac > V adc
            if i != 7:
                if comp.is_power():
                    binary = binary[:i] + '0' + binary[i + 1:]
                else:
                    binary = binary[:i] + '1' + binary[i + 1:]
            else:
                if comp.is_power():
                    binary = binary[:-1] + '0'
                else:
                    binary = binary[:-1] + '1'
            sleep(0.01)

        print(f"voltage DAC = {int(binary, 2) / 256 * 3.3} V")
        sleep(2)

except Exception as error:
    print(str(error))
finally:
    all_off()
