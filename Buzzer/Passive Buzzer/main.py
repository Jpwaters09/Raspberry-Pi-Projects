################################################
## Passive Buzzer                             ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Contact me: jpwaters.github@gmail.com      ##
################################################

from gpiozero import TonalBuzzer, Button
from gpiozero.tones import Tone
import math
from time import sleep

buzzer = TonalBuzzer(21)
button = Button(20)

def alertor():
  for x in range(0, 361):
    sinVal = Math.sin(x * (Math.pi / 18.0))
    toneVal = 2000 + sinVal * 500
    b.play(Tone(toneVal))
    sleep(0.001)

while True:
  if button.value == 1:
    alertor()
  else:
    buzzer.stop()
