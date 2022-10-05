from package.oop.oop import *
from package.constants import *
from time import sleep

dac = init_pins(ports_dac)

n = 0
try:
    t = int(input())
    assert 0 < t < 1000
    while True:
        n = bin(n % 256)[2:].zfill(8)
        binary_to_leds(dac, n)
        n += 1
        if n > 10 ** 10:
            n = 0

except Exception:
    raise ValueError("error")

finally:
    all_off()
