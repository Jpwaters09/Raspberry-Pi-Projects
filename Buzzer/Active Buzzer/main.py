################################################
## Active Buzzer                              ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Contact me: jpwaters.github@gmail.com      ##
################################################

from gpiozero import Buzzer, Button

buzzer = Buzzer(21)
button = Button(20)

while True:
  if button.value == 1:
    buzzer.on()
  if button.value == 0:
    buzzer.off()
