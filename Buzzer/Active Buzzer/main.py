################################################
## Active Buzzer                              ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Contact me: jpwaters.github@gmail.com      ##
## Follow my WhatsApp Channel: bit.ly/3sr99ZO ##
################################################

from gpiozero import Buzzer, Button

buzzer = Buzzer(21)
button = Button(20)

while True:
  if button.value == 1:
    buzzer.on()
  else:
    buzzer.off()
