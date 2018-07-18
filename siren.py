#!/usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
from time import sleep

SOUNDER = 26
Pi_Hz = 960    # For home use 850
Po_Hz = 770    # For home use 680

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER, GPIO.OUT, initial = GPIO.LOW)

p = GPIO.PWM(SOUNDER, 1)

p.start(50)

for i in range(0, 5) :
    p.ChangeFrequency(Pi_Hz)
    sleep(0.65)
    p.ChangeFrequency(Po_Hz)
    sleep(0.65)

p.stop()
GPIO.cleanup()
