from gpiozero import LED, Button
from signal   import pause
import os

led     = LED(17)
button  = Button(4)
running = False

button.when_pressed = led.toggle

pause()