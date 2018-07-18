import RPi.GPIO as GPIO
from time import sleep
import subprocess

def defSwitchLCD(channel):
    cmd = "python kirakira.py"
    if channel == 21:
        subprocess.call(cmd, shell=True)

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(21, GPIO.RISING, callback=defSwitchLCD, bouncetime=200)

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

