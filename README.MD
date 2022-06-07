# Football Table Gamification

This project is a simple MicroPython application that will run on Raspberry Pico. It will be able to detect when goal is achieved and by which team.

## Requirements

We will need the following hardware:

* Raspberry Pico (Brains)
* 2x 7 Segment display (Scoreboard)
* 2x IR LED Transmitter (To transmit IR light)
* 2x IR LED Receiver (To receive IR Light)
* Some cable for wiring up everything

## How it works

This is a really simple program:

Pico will simply detect when IR Beam is broken and add a score to the team that scored a goal. For goal detection we will use simple IR Light and for scoreboard we will use 7 segment display. When team reaches 10 goals, score is reset.

TODO: We could add some sort of animation for winning team.

We will be using the following GPIO pins: `17,16,14,13,12,18,19` for **1st 7 segment display**, pin `6` for Team 1 goal detection, `21,20,10,9,7,22,26` for **2nd 7 segment display** and pin `5` for Team 2 goal detection.

If you want to display dots, you can connect pins `15` and `11`.

Please note that wiring can differ for your 7 segment display, please check wiring in documentation for your hardware to avoid burning out LEDs and or Pico!


## Wiring Diagram

![Football-Table-Gamification-Wiring-Schema](/Images/Football-Table-Gamification-Wiring-Schema.png)

## Building the table

Step 1: Find a place for sensors
![IR Sensors 1](/Images/IMG_1622.jpeg)

Step 2: Secure sensors with tape/screw
![IR Sensors 2](/Images/IMG_1634.jpeg)

Step 3: Secure everything in place
![IR Sensors 3](/Images/IMG_1624.jpeg)

Step 4: Wire everything up and secure all of the cables.
![Wiring](/Images/IMG_1651.jpeg)


