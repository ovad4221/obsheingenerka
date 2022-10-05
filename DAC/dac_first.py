from oop.oop import *
from constants import *

dac = init_pins(ports_dac)

try:
    while True:
        try:
            print('enter %:')
            n = input()
            if n == 'q':
                break
            n = int(n)
            if n == -1:
                break
            for i in dac:
                dac[i].volt_perc(n)
        except ValueError:
            print("n must be a digit or 'q'")

except Exception:
    raise ValueError("ZALUPA PENIS HUI")

finally:
    all_off()
