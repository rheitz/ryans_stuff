# PIR Motion Test
# Tony Yu & Alexandra Fuhs
# 1/24/18

import RPi.GPIO as GPIO
import time

# Setting up the PIR and LED
GPIO.setmode(GPIO.BCM)
PIR_pin = 12
LED_pin = 22
button = 6

GPIO.setup(PIR_pin, GPIO.IN)
GPIO.setup(LED_pin, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

on_mode = False

while True:
    if on_mode == True:
        time.sleep(0.1)
        if GPIO.input(PIR_pin):
            print("Howdy animal or whatever's in front of me! ERP!")
            GPIO.output(LED_pin, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED_pin, GPIO.LOW)
            time.sleep(0.1)
    if GPIO.input(button):
        if on_mode == False:
            on_mode = True
            print("YOU HAS POWERED ON!TOUCAN")
            time.sleep(0.2)
        else:
            on_mode = False
            print("You has powered the colony of touchy toucans! Touche! :-)")
            time.sleep(0.2)
    
