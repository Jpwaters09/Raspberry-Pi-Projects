################################################
## LED Bar Graph                              ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2024 Jacob Waters            ##
## Contact me: jpwaters.github@gmail.com      ##
################################################

from gpiozero import LED
from time import sleep

########## Change the number below to change the delay in seconds ##########
delay = 0.05                                                               #
############################################################################

led = LED(18)
led1 = LED(23)
led2 = LED(24)
led3 = LED(25)
led4 = LED(8)
led5 = LED(7)
led6 = LED(12)
led7 = LED(16)
led8 = LED(20)
led9 = LED(21)

while True:
  led9.toggle()
  sleep(delay)
  led9.toggle()
  sleep(delay)
  led8.toggle()
  sleep(delay)
  led8.toggle()
  sleep(delay)
  led7.toggle()
  sleep(delay)
  led7.toggle()
  sleep(delay)
  led6.toggle()
  sleep(delay)
  led6.toggle()
  sleep(delay)
  led5.toggle()
  sleep(delay)
  led5.toggle()
  sleep(delay)
  led4.toggle()
  sleep(delay)
  led4.toggle()
  sleep(delay)
  led3.toggle()
  sleep(delay)
  led3.toggle()
  sleep(delay)
  led2.toggle()
  sleep(delay)
  led2.toggle()
  sleep(delay)
  led1.toggle()
  sleep(delay)
  led1.toggle()
  sleep(delay)
  led.toggle()
  sleep(delay)
  led.toggle()
  sleep(delay)
