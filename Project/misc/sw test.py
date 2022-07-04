import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
os.system("python3 /home/pi/Nandas/gr.py")

while True:
    input_state = GPIO.input(40)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
