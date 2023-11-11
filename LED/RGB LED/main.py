##############################################
# RGB LED                                    #
# Author: Jacob Waters                       #
# Github: github.com/jpwaters09              #
# Contact me: jpwaters.github@gmail.com      #
# Follow my WhatsApp Channel: bit.ly/3sr99ZO #
##############################################

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

def r():
  r.on()

def g():
  g.on()

def b():
  b.on()

def off():
  r.off()
  g.off()
  b.off()

while True:
  r()
  sleep(delay)
  off()
  g()
  sleep(delay)
  off()
  b()
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
