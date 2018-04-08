# Tony Yu
# 1/3/18
# Light Up Guessing Game
# Guess a number from 1 to 20, shows blue if too low, shows red if too high, shows green if correct.
# 5 tries

import random
import time
import RPi.GPIO as GPIO

def game_over():
    print("Well 5 guesses is up.")
    time.sleep(2)
    print("GAME OVER. YOU LOSE. BOO HOO lel")
    time.sleep(0.8)

def blink_LED(pin):
    for i in range(5):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.2)

def blink_AQIB():
    for i in range(2):
        pwm_red.start(90)
        pwm_green.start(10)
        pwm_blue.start(10)
        time.sleep(1)
        print(i)
        pwm_red.stop()
        pwm_green.stop()
        pwm_blue.stop()
        
# LED pin setup
GPIO.setmode(GPIO.BCM)
LED_pin_apple = 21 
LED_pin_grass = 22
LED_pin_blueberry = 23

GPIO.setup(LED_pin_apple, GPIO.OUT)
GPIO.setup(LED_pin_grass, GPIO.OUT)
GPIO.setup(LED_pin_blueberry, GPIO.OUT)

pwm_red = GPIO.PWM(LED_pin_apple,100)
pwm_green = GPIO.PWM(LED_pin_grass,100)
pwm_blue = GPIO.PWM(LED_pin_blueberry,100)

# Title and instructions
print("N"*80)
print("WELCOME TO THE AWESOME GUESSING GAME")
print("N"*80)
time.sleep(1)
print("""
You have 5 guesses to guess a number in between 1 and 20!
The light will blink:
Red = Too hot(a.k.a high)
Green = Just right
Blue = Too cold(a.k.a low)
""")
time.sleep(4)
print("Now there Goldilocks go on to drink your soups")

play_again = "Y"

while play_again == "Y":

    # Get a random number (1 to 20)
    num = random.randint(1, 20)

    # Get the guess and put in the loop
    guesses = 0
    while guesses < 5:
        guess = input("Now guess the number: ")
        guess = int(guess)
        guesses += 1
        # Check if correct
        if guess == num:
            print("Correct!")
            blink_LED(LED_pin_grass)
            print("YOU WIN!!!")
            break
        elif guess < num:
            print("Too Low!")
            blink_LED(LED_pin_blueberry)
        elif guess == 21:
            print("ACTIVATING AQIBA TALIBA MODE")
            time.sleep(2)
            print("WELCOME AQIBA")
            time.sleep(3)
            print("Ok den you WIN cuz u iz aqib and aqib always win")
            time.sleep(5)
            print("Lel nope just kidding you lose")
            time.sleep(8)
            print("ACTUALLY YOU WIN!!!! NO KIDDING LOLEOLOELFOELEOLOFELOELFOEFLEOFLEOF")
            break
        elif guess > num:
            print("Too High!")
            blink_LED(LED_pin_apple)
    else:
        game_over()
    play_again = input("Do you want to play again?(y/n): ").upper()
    

          
