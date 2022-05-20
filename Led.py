import RPi.GPIO as GPIO
import time
import os, sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#setup output pins
GPIO.setup(38, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#define 7 segment digits
digitclr=[0,0,0,0,0,0,0]
digit0=[1,1,1,1,1,1,0]
digit1=[0,1,1,0,0,0,0]
digit2=[1,1,0,1,1,0,1]
digit3=[1,1,1,1,0,0,1]
digit4=[0,1,1,0,0,1,1]
digit5=[1,0,1,1,0,1,1]
digit6=[1,0,1,1,1,1,1,]
digit7=[1,1,1,0,0,0,0]
digit8=[1,1,1,1,1,1,1]
digit9=[1,1,1,0,0,1,1,]
gpin=[38,24,40,32,36,26,18]
#routine to clear and then write to display
def digdisp(digit):
    for x in range (0,7):
        GPIO.output(gpin[x], digitclr[x])
    for x in range (0,7):
        GPIO.output(gpin[x], digit[x])
#routine to display digit from 0 to 9

while True:
    digdisp(digit0)
    time.sleep(0.3)
    digdisp(digit1)
    time.sleep(0.3)
    digdisp(digit2)
    time.sleep(0.3)
    digdisp(digit3)
    time.sleep(0.3)
    digdisp(digit4)
    time.sleep(0.3)
    digdisp(digit5)
    time.sleep(0.3)
    digdisp(digit6)
    time.sleep(0.3)
    digdisp(digit7)
    time.sleep(0.3)
    digdisp(digit8)
    time.sleep(0.3)
    digdisp(digit9)
    time.sleep(0.3)
#tidy up

GPIO.cleanup()
import sys
sys.exit()
