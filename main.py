from machine import Pin as P
import time as t
#Code for blinking a led
led=P(2,P.OUT)

while True:
    led.value(0)
    t.sleep(1)
    led.value(1)
    t.sleep(1)
