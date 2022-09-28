import RPi.GPIO as gpio
from time import sleep
from oop import *
from random import randint

gpio.setmode(gpio.BCM)

ports_dac = [26, 19, 13, 6, 5, 11, 9, 10]
ports_leds = [21, 20, 16, 12, 7, 8, 25, 24]
diods_dac = []
diods_leds = []
for i in range(1, 9):
    # exec(f"diod{i} = Diod({ports[i - 1]})")
    diods_dac.append(Diod(ports_dac[i - 1]))
    diods_leds.append(Diod(ports_leds[i - 1]))


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
    

all_off(diods_dac)
all_off(diods_leds)
