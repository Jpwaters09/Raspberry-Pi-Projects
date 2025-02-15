################################################
## LED Push Button                            ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2025 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from gpiozero import LED, Button

button = Button(20)
led = LED(21)

while True:
  if button.value == 0:
    led.on()
  if button.value == 1:
    led.off()
