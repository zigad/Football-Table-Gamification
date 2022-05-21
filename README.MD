# Football Table Gamification

This project is a simple python application that will run on Raspberry Pi Zero. It will be able to detect when goal is achieved and by which team.

## Requirements

We will need the following hardware:
* Raspberry Pi Zero W (Brains)
* 2x 7 Segment display (Scoreboard)
* 2x IR LED Transmitter (To transmit IR light)
* 2x IR LED Receiver (To receive IR Light)


## How it works
This is a simple program:

Raspberry Pi will simply detect when IR Beam is breaked and add a score to the team that scored a goal. For goal detection we will use simple IR Light and for scoreboard we will use 7 segment display.

We are currently using physical pins 38,24,40,32,36,26,18 for 1st 7 segment display, pin 27 for Team 1 goal detection and pin 17 for Team 2 goal detection