##############################################
# LED Blink                                  #
# Author: Jacob Waters                       #
# Github: github.com/jpwaters09              #
# Contact me: jpwaters.github@gmail.com      #
# Follow my WhatsApp Channel: bit.ly/3sr99ZO #
##############################################

from gpiozero import LED
from time import sleep

########## Change the number below to change the delay in seconds ##########
delay = 0.5                                                              #
##########################################################################

led = LED(21)

while True:
  led.toggle()
  sleep(delay)
