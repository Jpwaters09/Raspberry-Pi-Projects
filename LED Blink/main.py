################################################
## LED Blink                                  ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2024 Jacob Waters            ##
## Contact me: jpwaters.github@gmail.com      ##
################################################

from gpiozero import LED
from time import sleep

########## Change the number below to change the delay in seconds ##########
delay = 0.5                                                                #
############################################################################

led = LED(21)

while True:
  led.toggle()
  sleep(delay)
