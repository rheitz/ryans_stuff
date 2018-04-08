# DJ Raspi
# Tony Yu
# 1/16/18
# Turn the Raspberry Pi into a Dj

# Imports stuff
import RPi.GPIO as GPIO
import time
import random
import os

# Variable creation for sound folders
path_music = "/usr/share/scratch/Media/Sounds/Music Loops/"
path_vocals = "/usr/share/scratch/Media/Sounds/Vocals/"
path_effects = "/usr/share/scratch/Media/Sounds/Effects/"

# Returns a list of MP3 sounds for the path given
def get_MP3_sounds(sound_path):
    sound_filesound_files = os.listdir(sound_path)
    sound_filesound_files = [sound_file for sound_file in sound_filesound_files]
    return sound_filesound_files

# Plays a random sound from a list of MP3s for the path given
def play_random_sound(sound_path, sound_files):           
    sound_file = random.choice(sound_files)
    os.system("omxplayer -o local '" + sound_path + "/" + sound_file + "' &")

# Get the list of music loops and vocals (MP3s only)
sounds_music = get_MP3_sounds(path_music)
sounds_vocals = get_MP3_sounds(path_vocals)
sounds_effects = get_MP3_sounds(path_effects)
                
# Variables for button pins
button_pin1 = 6 
button_pin2 = 19

# Set pin numbering
GPIO.setmode(GPIO.BCM)

# Setup GPIO for input
GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)

# Clears the screen
os.system("clear")

# Title
title = """
    THIS IS DA DJ RASPI
    Press Button1 for dem music loops
    Press Button2 for dem vocals
    Press Ctrl + C to kill dem program
"""

# Start infinite loop(Have to either destroy computer or press CTRL+C to kill it)
while True:
    if GPIO.input(button_pin1):
        print("You has pressed button 1")
        play_random_sound(path_music, sounds_music)
        time.sleep(0.1)
    if GPIO.input(button_pin2):
        print("You has pressed button 2")
        play_random_sound(path_vocals, sounds_vocals)
        time.sleep(0.1)
    if GPIO.input(button_pin1) and GPIO.input(button_pin2):
        print("You has pressed button 1 and 2! GOOD JOB EASTER BUN")
        play_random_sound(path_effects, sounds_effects)
        time.sleep(0.1)
    time.sleep(0.3)



        
