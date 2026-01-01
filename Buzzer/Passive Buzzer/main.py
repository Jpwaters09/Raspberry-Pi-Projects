################################################
## Passive Buzzer                             ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Copyright (c) 2026 Jacob Waters            ##
## Contact me: jpwaters09.business@gmail.com  ##
################################################

from gpiozero import TonalBuzzer, Button
from gpiozero.tones import Tone
from time import sleep

########## Change the number below to change the delay in seconds ##########
delay = 0.05                                                               #
############################################################################

buzzer = TonalBuzzer(21)
button = Button(20)

def alertor():
  buzzer.play(Tone(midi=57))
  sleep(delay)
  buzzer.play(Tone(midi=59))
  sleep(delay)
  buzzer.play(Tone(midi=61))
  sleep(delay)
  buzzer.play(Tone(midi=63))
  sleep(delay)
  buzzer.play(Tone(midi=65))
  sleep(delay)
  buzzer.play(Tone(midi=67))
  sleep(delay)
  buzzer.play(Tone(midi=69))
  sleep(delay)
  buzzer.play(Tone(midi=71))
  sleep(delay)
  buzzer.play(Tone(midi=73))
  sleep(delay)
  buzzer.play(Tone(midi=75))
  sleep(delay)
  buzzer.play(Tone(midi=77))
  sleep(delay)
  buzzer.play(Tone(midi=79))
  sleep(delay)
  buzzer.play(Tone(midi=81))
  sleep(delay)

while True:
  if button.value == 1:
    alertor()
  if button.value == 0:
    buzzer.stop()
