###########################################
# LED Push Button                         #
# Author: Jacob Waters                    #
# Github: github.com/jpwaters09           #
# Contact me: jpwaters.github@gmail.com   #
###########################################

from gpiozero import LED, Button
from time import sleep

button = Button(20)
led = LED(21)

while True:
  if button.value == 1:
    led.toggle()
    sleep(0.3)
