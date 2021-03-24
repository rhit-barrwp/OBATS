from gpiozero import LED, Button
from signal   import pause
import os

led     = LED(17)
button  = Button(4)
running = False


def start_read():
	if not running:
		print("Read Starting!")
		os.system("python /home/pi/OBATS/Master/master.py &")
		global running
		running = True
	else:
		print("Read Ending!")
		os.system("sudo pkill -f 'master.py'")
		global running
		running = False
	led.toggle()

button.when_pressed = start_read

pause()