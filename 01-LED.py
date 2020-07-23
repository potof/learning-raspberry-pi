# flash LED

import RPi.GPIO as GPIO

led_gpio = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_gpio, GPIO.OUT)

GPIO.output(led_gpio, True)
