from package.oop.oop import *
from package.constants import *

dac = init_pins(ports_dac)

try:
    while True:
        try:
            n = input()
            if n == 'q':
                break
            n = bin(int(n))[2:].zfill(8)
            binary_to_leds(dac, n, report=True)
        except ValueError:
            print("n must be a digit or 'q'")

except Exception:
    raise ValueError("error")

finally:
    all_off()
