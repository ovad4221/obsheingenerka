from package.oop.oop import *
from package.constants import *

dac = init_pins(ports_dac)
leds = init_pins(ports_leds)
all_off(how='ld_pins')
dc = int(input()) % 100
for i in range(len(leds)):
    leds[i].pwm.start(100 - dc)
old_dc = dc

try:
    while True:
        dc = int(input()) % 100
        for i in range(len(leds)):
            leds[i].change_dc(100 - dc)
            print(3.3 * dc / 100)

except Exception:
    raise ValueError("sth error")

finally:
    all_off()
