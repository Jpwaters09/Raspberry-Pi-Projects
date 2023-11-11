##############################################
# LED Push Button                            #
# Author: Jacob Waters                       #
# Github: github.com/jpwaters09              #
# Contact me: jpwaters.github@gmail.com      #
# Follow my WhatsApp Channel: bit.ly/3sr99ZO #
##############################################

from gpiozero import LED, Button

button = Button(20)
led = LED(21)

while True:
  if button.value == 1:
    led.on()
  else:
    led.off()
