## Face Recognition with Arduino LED Control

This project involves a face recognition system that compares a reference image with live video feed from a webcam. If the face matches, it sends a signal to an Arduino to light up a green LED. If the face does not match, it lights up a red LED. If no face is detected, the red LED remains on.

## Prerequisites
## Software
- [x] Python 3.11
- [x] OpenCV
- [X] face_recognition library
- [X] pySerial library
- [X] Arduino IDE
## Hardware
- [x] Arduino board
- [x] 2 LEDs (1 green and 1 red)
- [X] Resistors (220 ohm recommended)
- [X] Webcam

## Hardware Setup
- Connect the green LED to pin 10 of the Arduino, with the anode (longer leg) connected to the pin and the cathode (shorter leg) connected to ground through a resistor.
- Connect the red LED to pin 9 of the Arduino in a similar manner.
- Connect the Arduino to your computer via USB.
