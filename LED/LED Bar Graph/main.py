################################################
## LED Bar Graph                              ##
## Language: Python                           ##
## Author: Jacob Waters                       ##
## Github: github.com/jpwaters09              ##
## Contact me: jpwaters.github@gmail.com      ##
## Follow my WhatsApp Channel: bit.ly/3sr99ZO ##
################################################

from gpiozero import LED
from time import sleep

led = LED(18)
led1 = LED(23)
led2 = LED(24)
led3 = LED(25)
led4 = LED(8)
led5 = LED(7)
led6 = LED(12)
led7 = LED(16)
led8 = LED(20)
led9 = LED(21)

while True:
  led9.toggle()
  sleep(0.1)
  led9.toggle()
  sleep(0.1)
  led8.toggle()
  sleep(0.1)
  led8.toggle()
  sleep(0.1)
  led7.toggle()
  sleep(0.1)
  led7.toggle()
  sleep(0.1)
  led6.toggle()
  sleep(0.1)
  led6.toggle()
  sleep(0.1)
  led5.toggle()
  sleep(0.1)
  led5.toggle()
  sleep(0.1)
  led4.toggle()
  sleep(0.1)
  led4.toggle()
  sleep(0.1)
  led3.toggle()
  sleep(0.1)
  led3.toggle()
  sleep(0.1)
  led2.toggle()
  sleep(0.1)
  led2.toggle()
  sleep(0.1)
  led1.toggle()
  sleep(0.1)
  led1.toggle()
  sleep(0.1)
  led.toggle()
  sleep(0.1)
  led.toggle()
  sleep(0.1)
