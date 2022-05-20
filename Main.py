import RPi.GPIO as GPIO

BEAM_PIN_1 = 27
BEAM_PIN_2 = 17

def break_beam_callback_1(channel):
    if GPIO.input(BEAM_PIN_1):
         print("Team 1 Goal!")

def break_beam_callback_2(channel):
    if GPIO.input(BEAM_PIN_2):
         print("Team 2 Goal!")


GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BEAM_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(BEAM_PIN_1, GPIO.BOTH, callback=break_beam_callback_1)
GPIO.add_event_detect(BEAM_PIN_2, GPIO.BOTH, callback=break_beam_callback_2)

message = input("Press enter to quit\n\n")

GPIO.cleanup()
