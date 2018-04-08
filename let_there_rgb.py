# Tony Yu
# 1/3/18
# RGB LIGHT

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin_apple = 21
led_pin_grass = 22
led_pin_blue = 23

GPIO.setup(led_pin_apple, GPIO.OUT)
GPIO.setup(led_pin_grass, GPIO.OUT)
GPIO.setup(led_pin_blue, GPIO.OUT)

pwm_red = GPIO.PWM(led_pin_apple,100)
pwm_green = GPIO.PWM(led_pin_grass,100)
pwm_blue = GPIO.PWM(led_pin_blue,100)

pwm_red.start(10)
pwm_green.start(50)
pwm_blue.start(15)
time.sleep(0.5)

pwm_red.stop()
pwm_green.stop()
pwm_green.stop()
GPIO.cleanup()
