from package.oop.oop import *
from package.constants import *
from random import randint

diods_dac = init_pins(ports_dac)
diods_leds = init_pins(ports_leds)


for i in range(2):
    run_zm(diods_dac, 0.05)
    run_zm(diods_leds, 0.05)

binary = ''.join([str(randint(0, 1)) for _ in range(8)])
binary_old = binary
binary_to_leds(diods_dac, binary)
# print(numbers)

while True:
    x = int(input())

    if x == -1:
        break
    binary = str(bin(x))[2:].rjust(8, '0')
    # print(binary)
    flag = binary_to_leds(diods_dac, binary)
    if flag:
        binary_to_leds(diods_leds, binary_old)
    binary_old = binary
    

all_off()