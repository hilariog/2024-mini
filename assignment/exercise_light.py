#!/usr/bin/env python3
"""
Use analog input with photocell
"""

import time
import machine

# GP28 is ADC2
ADC2 = 28

led = machine.Pin(25, machine.Pin.OUT)
adc = machine.ADC(ADC2) #adc28

blink_period = 0.1

max_bright = 30000 #play with these
min_bright = 6300


def clip(value: float) -> float:
    """clip number to range [0, 1]"""
    if value < 0:
        return 0
    if value > 1:
        return 1
    return value

machine.Pin(25, machine.Pin.OUT).high
while True:
    value = adc.read_u16()
    print(value)
    """
    need to clip duty cycle to range [0, 1]
    this equation will give values outside the range [0, 1]
    So we use function clip()
    """

    duty_cycle = clip((value - min_bright) / (max_bright - min_bright))# want min bright to equal value at low, and max bright to equal value at high


    #led.high()
    time.sleep(blink_period * duty_cycle)#we want basically full bkink period sleep when high and zero sleep when low i.e, duty_cycle = 1 and 0

    #led.low()
    time.sleep(blink_period * (1 - duty_cycle))
