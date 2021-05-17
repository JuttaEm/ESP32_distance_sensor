# only for preliminary testing with esp, not relevant to the distance sensor

import time
from machine import Pin

led = Pin(18, Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
