# IOT Based Smart Parking

## ABSTRACT

We successfully implemented an IOT based smart parking system. With the help of individual nodes (proximity sensors) at every parking slot, we can reflect live parking slot status – ‘Available’ or ‘Occupied’ - on the internet.

### ISSUES WITH CURRENT SYSTEM

1. Parking counters don’t exactly specify where slots are available
2. Light Indicators don’t fully resolve the problem
3. Absence of autonomous billing

## PROPOSED SYSTEM

1. Access information about each parking slots via the internet
2. Live availability information will help find parking spots faster
3. Autonomous billing will further ease the process

[GIF]

## Hardware Requirements

We plan to start with a small-scale implementation of the project i.e. simulate a real-life parking lot on a cardboard.

ELECTRONIC COMPONENTS
1. Raspberry Pi (Main control unit)
2. IR Sensor (Proximity Sensors)
3. RF id Reader
4. RF id Cards
CAUTION : Make sure that the operational frequency of the RF id Reader is the same as the ID cards!!

## Software Implementation

The project has two different python programs running simultaneously

### 1. RF-ID Tagging Module
This program takes care of authentication of the RF-ID cards. Controls the micro servo motor (acts as a gate) and logs in/out time. This is the program that sends out mails based on the total time the user spends in the Parking lot. The customer will have to interact with this program and hence ease of use along with clarity of information was given importance.

### 2. Proximity Sensors Module
This program reflects the current status of the sensors – ‘high’ or ‘low’. These sensors reflect the slot availability – ‘Available’ or ‘Occupied’. The Output is then dumped onto a text file, which is updated every second using the same python script. Furthermore, a HTML file reads the data from the text file and displays it onto the webpage. We then host the website using a hosting service called ‘ngrok’. Hence the server contains information about the availability status of the respective parking slots.

## Code and Software Implemetaion

BASIC KNOWLEDGE OF PYTHON & LINUX ENVIRONMENT REQUIRED

1. Start by loading and running RaspbianOs on the RaspberryPi.
2. All Files other than 'READ.py' help in interfacing (between sensors, Readers, Motors and the Microcontroller) and hence the code need not be changed.
3. Alter 'READ.py' appropriately by following comments.

## Flowchart

## Project Video

[LINK]

## # Directory Structure
- ```src``` folder contains the source code. 
- ```results``` folder contains animation frames
