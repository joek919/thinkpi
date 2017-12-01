import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(17)
    if input_state == False:
        print('switch is on')
    if input_state == True:
        print('switch is off')
    time.sleep(2.0)
