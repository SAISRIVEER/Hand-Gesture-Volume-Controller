# Hand-Gesture-Volume-Controller
# Overview
This project implements a hand gesture volume controller using a webcam feed to detect hand movements. It uses OpenCV for video capture, MediaPipe for hand tracking, and PyCaw to interface with system audio. The project maps finger distances to control the system volume.


# Features
 Detects hand landmarks using a webcam.
 Calculates the distance between the thumb and index finger.
 Maps this distance to the system's volume level.
 Visualizes the gesture and volume change on the screen.


# Requirements
 Python 3.x
 OpenCV
 MediaPipe
 PyCaw
 Numpy


# Instructions
Make sure your webcam is connected and working.
Use your thumb and index finger to adjust the system volume.
The volume will change based on the distance between your fingers.
