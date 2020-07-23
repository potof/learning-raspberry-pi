# flashing LED

import RPi.GPIO as GPIO
import time 


led_gpio = 18

waitsec = 0.5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_gpio, GPIO.OUT)

for i in range(20):
    GPIO.output(led_gpio, True)
    time.sleep(waitsec)
    GPIO.output(led_gpio, False)
    time.sleep(waitsec)

GPIO.cleanup()
