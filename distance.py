from machine import Pin
import hcsr04

hcsr = hcsr04.HCSR04(25, 27)


def get_distance():
    return hcsr.distance_cm()
