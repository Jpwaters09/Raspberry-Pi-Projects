################################################
## LED Push Button Toggle                     ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2026 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from gpiozero import LED, Button
from time import sleep

button = Button(20)
led = LED(21)

led.off()

while True:
  if button.value == 1:
    led.toggle()
    sleep(0.3)
