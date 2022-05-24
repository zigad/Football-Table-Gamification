from machine import Pin
import time

score_team_1 = 0
score_team_2 = 0

display_list_1 = [17,16,14,13,12,18,19]
display_list_2 = [21,20,10,9,7,22,26]
dotPin1=15
dotPin2=11
display_obj_team_1 = []
display_obj_team_2 = []


BeamPin1 = machine.Pin(28, machine.Pin.IN)
BeamPin2 = machine.Pin(27, machine.Pin.IN)

# Set all pins as output
for seg1 in display_list_1:
    display_obj_team_1.append(Pin(seg1, Pin.OUT))

dot_obj1=Pin(dotPin1, Pin.OUT)

# Set all pins as output
for seg2 in display_list_2:
    display_obj_team_2.append(Pin(seg2, Pin.OUT))

dot_obj2=Pin(dotPin2, Pin.OUT)

# DIGIT map as array of array
arrSegTeam = [[1,1,1,1,1,1,0],\
          [0,1,1,0,0,0,0],\
          [1,1,0,1,1,0,1],\
          [1,1,1,1,0,0,1],\
          [0,1,1,0,0,1,1],\
          [1,0,1,1,0,1,1],\
          [1,0,1,1,1,1,1],\
          [1,1,1,0,0,0,0],\
          [1,1,1,1,1,1,1],\
          [1,1,1,1,0,1,1]]

def SegDisplayTeam1(toDisplay):
    numDisplay = int(toDisplay.replace(".", ""))
    for a in range(7):
        display_obj_team_1[a].value(arrSegTeam[numDisplay][a])
    # Manage DOT activation
    if toDisplay.count(".") == 1:
        dot_obj1.value(1)
    else:
        dot_obj1.value(0)
        
def SegDisplayTeam2(toDisplay):
    numDisplay = int(toDisplay.replace(".", ""))
    for a in range(7):
        display_obj_team_2[a].value(arrSegTeam[numDisplay][a])
    # Manage DOT activation
    if toDisplay.count(".") == 1:
        dot_obj2.value(1)
    else:
        dot_obj2.value(0)
        
def resetGame():
    global score_team_1
    global score_team_2
    score_team_1 = 0
    score_team_2 = 0
    SegDisplayTeam1(str(0))
    SegDisplayTeam2(str(0))

def break_beam_callback_1(pin):
    if pin is BeamPin1:
        global score_team_1
        score_team_1 = score_team_1 + 1
        if score_team_1 == 10:
            resetGame()
        SegDisplayTeam1(str(score_team_1))
        print("Team 1 Goal!")
    
    if pin is BeamPin2:
        global score_team_2
        score_team_2 = score_team_2 + 1
        if score_team_2 == 10:
            resetGame()
        SegDisplayTeam2(str(score_team_2))
        print("Team 2 Goal!")
        
SegDisplayTeam1(str(0))
SegDisplayTeam2(str(0))

BeamPin1.irq(trigger=Pin.IRQ_RISING, handler=break_beam_callback_1)
BeamPin2.irq(trigger=Pin.IRQ_RISING, handler=break_beam_callback_1)
