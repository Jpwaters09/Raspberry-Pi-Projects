################################################
## Passive Buzzer                             ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Contact me: jpwaters.github@gmail.com      ##
################################################

from gpiozero import TonalBuzzer, Button
from gpiozero.tones import Tone
from time import sleep

buzzer = TonalBuzzer(21)
button = Button(20)

def alertor():
  buzzer.play(Tone(midi=57))
  sleep(0.1)
  buzzer.play(Tone(midi=59))
  sleep(0.1)
  buzzer.play(Tone(midi=61))
  sleep(0.1)
  buzzer.play(Tone(midi=63))
  sleep(0.1)
  buzzer.play(Tone(midi=65))
  sleep(0.1)
  buzzer.play(Tone(midi=67))
  sleep(0.1)
  buzzer.play(Tone(midi=69))
  sleep(0.1)
  buzzer.play(Tone(midi=71))
  sleep(0.1)
  buzzer.play(Tone(midi=73))
  sleep(0.1)
  buzzer.play(Tone(midi=75))
  sleep(0.1)
  buzzer.play(Tone(midi=77))
  sleep(0.1)
  buzzer.play(Tone(midi=79))
  sleep(0.1)
  buzzer.play(Tone(midi=81))
  sleep(0.1)

while True:
  if button.value == 1:
    alertor()
  if button.value == 0:
    buzzer.stop()
