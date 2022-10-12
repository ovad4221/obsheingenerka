from package.oop.oop import *
from package.constants import *
from time import sleep

dac = init_pins(ports_dac)
all_off(how='ld_pins', pins=dac)

flag = True
n = 0
try:
    t = int(input()) / 256
    assert 0 < t < 1000
    while True:
        binary_to_leds(dac, bin(n % 256)[2:].zfill(8))
        if flag:
            n += 1
        else:
            n -= 1
        if n % 256 == 255 or n % 256 == 0:
            flag = not flag
        sleep(t)

except Exception:
    raise ValueError("error")

finally:
    all_off()
