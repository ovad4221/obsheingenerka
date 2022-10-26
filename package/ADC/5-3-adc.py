from package.oop.oop import *
from package.constants import *
from time import sleep

dac = init_pins(ports_dac)
leds = init_pins(ports_leds)
comp = Pin_In(4)
troyka = Pin_Out(17, initial=True)

try:
    while True:
        # 0 1 0 1 1 1 1 0
        binary = [1, 0, 0, 0, 0, 0, 0, 0]
        for i in range(8):
            binary_to_leds(dac, ''.join([str(i) for i in binary]))
            sleep(0.001)
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

        print(f"voltage DAC = {int(''.join([str(i) for i in binary]), 2) / 256 * 3.3} V")
        st_one = '1' * int(int(''.join([str(i) for i in binary]), 2) / 256) * 100
        binary_to_leds(leds, st_one.zfill(8))
        sleep(0.5)

except Exception as error:
    print(str(error))
finally:
    all_off()
