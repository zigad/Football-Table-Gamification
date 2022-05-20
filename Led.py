import RPi.GPIO as IO
import time 

DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67] 
IO.setwarnings(False)
IO.setmode (IO.BCM)

IO.setup(38, IO.OUT)
IO.setup(24, IO.OUT)
IO.setup(40, IO.OUT)
IO.setup(32, IO.OUT)
IO.setup(36, IO.OUT)
IO.setup(26, IO.OUT)
IO.setup(18, IO.OUT)

def PORT(pin):
    if(pin&0x01 == 0x01):
        IO.output(13,1) 
    else:
        IO.output(13,0)
    if(pin&0x02 == 0x02):

        IO.output(6,1)
    else:

        IO.output(6,0)
    if(pin&0x04 == 0x04):

        IO.output(16,1)

    else:

        IO.output(16,0)

    if(pin&0x08 == 0x08):

        IO.output(20,1)

    else:

        IO.output(20,0)   

    if(pin&0x10 == 0x10):

        IO.output(21,1)

    else:

        IO.output(21,0)

    if(pin&0x20 == 0x20):

        IO.output(19,1)

    else:

        IO.output(19,0)

    if(pin&0x40 == 0x40):

        IO.output(26,1)

    else:

        IO.output(26,0)

    if(pin&0x80 == 0x80):

        IO.output(12,1)
    else:

        IO.output(12,0)
        

while 1:

    for x in range(10):
        pin = DISPLAY[x]
        PORT(pin)
        time.sleep(1)
