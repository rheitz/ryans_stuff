# Tony Yu
# 12/19/17
# LET THERE BEE LIGHT

import RPi.GPIO as GPIO
import time

# Variable for the GPIO pin number
LED_pin_apple = 21
LED_pin_grass = 20
LED_pin_blue = 16

# Tells the Pi we be using the breakout board numbering
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for output
GPIO.setup(LED_pin_apple, GPIO.OUT)
GPIO.setup(LED_pin_grass, GPIO.OUT)
GPIO.setup(LED_pin_blue, GPIO.OUT)

# Loop to blink the LED
while True:
    GPIO.output(LED_pin_apple, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(LED_pin_apple, GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(LED_pin_grass, GPIO.HIGH)
    time.sleep(0.02)
    GPIO.output(LED_pin_grass, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(LED_pin_blue, GPIO.HIGH)
    time.sleep(0.03)
    GPIO.output(LED_pin_blue, GPIO.LOW)
    time.sleep(0.03)


