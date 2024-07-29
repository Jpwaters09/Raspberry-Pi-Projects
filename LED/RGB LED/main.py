################################################
## RGB LED                                    ##
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

r = LED(21)
g = LED(20)
b = LED(16)

def rg():
  r.on()
  g.on()

def rb():
  r.on()
  b.on()

def gb():
  g.on()
  b.on()

def red():
  r.on()

def green():
  g.on()

def blue():
  b.on()

def off():
  r.off()
  g.off()
  b.off()

while True:
  red()
  sleep(delay)
  off()
  green()
  sleep(delay)
  off()
  blue()
  sleep(delay)
  off()
  rg()
  sleep(delay)
  off()
  rb()
  sleep(delay)
  off()
  gb()
  sleep(delay)
  off()
