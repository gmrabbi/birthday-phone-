import pygame
import os
import sys
import datetime
from time import sleep
from pygame.locals import *

pygame.mixer.init()
happyBirthday = pygame.mixer.Sound("Happy_Birthday_To.wav")
# happyBirthday.play()
beep = pygame.mixer.Sound("beep.wav")


print("Hi, What's your Name.?")
beep.play()
name = str(input())
sleep(0.5)
beep.play()
print("How are you " + name + " ?")
beep.play()
input("> ")
beep.play()
print("\nWait there is one message for you..\n")
beep.play()
sleep(1)

lst = ["                  i i i i i",
       "                  i i i i i",
       "                 _i_i_i_i_i_",
       "              :❤           ❤ :",
       "            __: ❤ 02/12/2001❤  :__",
       "           : ❤   ❤        ❤   ❤  :",
       "         __: ❤   HAPPY     ❤   ❤ :__",
       "        : ❤  ❤       BIRTHDAY   ❤   :",
       "        : ❤   ❤     ❤    ❤    ❤  ❤  :",
       "        : ❤ Soumitra Sarkar Hira  ❤ :",
       "        :___________________________:"]

happyBirthday.play()
for line in lst:
    print(line)
    sleep(1)
    beep.play()

message = "Have a Good Day.."
for i in message:
    print(i, end="")


print("\n")
file = open("name.txt", "r")
for line in file.readlines():
    print(line, end="")
    sleep(0.5)
    beep.play()
print("\nLet's Celebrate..👋👋👋👋👋👋")
birthday = pygame.mixer.Sound("Traditional-Happy-Birthday-To-You-Song.mp3")
birthday.play()
sleep(21)


# to python3.x
#from urllib.request import urlopen


# pyaud = pyaudio.PyAudio()

# srate = 44100

# stream = pyaud.open(format=pyaud.get_format_from_width(1),
#                     channels=1,
#                     rate=srate,
#                     output=True)


# url = "/files/download/id/1384"
# u = urlopen(url)

# data = u.read(8192)

# while data:

#     stream.write(data)
#     data = u.read(8192)
