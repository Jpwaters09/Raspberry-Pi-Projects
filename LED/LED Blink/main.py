from gpiozero import LED
from time import sleep

##########Change the number below to change the delay##########
delay = 1                                                     #
###############################################################

led = LED(21)

while True:
  led.toggle()
  sleep(delay)
