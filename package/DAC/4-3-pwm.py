from package.oop.oop import *
from package.constants import *

dac = init_pins(ports_dac)
leds = init_pins(ports_leds)
all_off(how='ld_pins', pins=dac + leds)
dc = int(input()) % 100
for i in range(len(dac)):
    dac[i].pwm.start(dc)
old_dc = dc
for i in range(len(leds)):
    leds[i].pwm.start(dc)

try:
    while True:
        dc = int(input()) % 101
        for i in range(len(dac)):
            dac[i].change_dc(dc)
            print(f"DAC current voltage {3.3 * dc / 100} V")

        for i in range(len(leds)):
            leds[i].change_dc(old_dc)
            print(f"LEDs current voltage {3.3 * old_dc / 100} V")
        old_dc = dc


except Exception:
    raise ValueError("sth error")

finally:
    all_off()
