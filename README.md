# Gakken Eye Tracker
## Overview:
This project aims to make a virtual eye look at points of interest such as faces. To achieve this a raspberry pi is used to display the eye and recieve commands. A seperate web server is then used to track objects from a camera and send it to the raspberry pi.

## Installation:
![Install.md](install.md)

## Flow chart:
[](flowchart.png)
## Files:
- **eye.py:**
This is the main program that runs on the raspberry pi. It displays the 3d eye onto the display and also connects to the websocket server to recieve data. Incoming data must follow this structure:
`"X,Y,Z,B"`.
    - X = X-Coordinate, Float between 0 and 1.
    - Y = Y-Coordinate, Float between 0 and 1.
    - Z = Iris value, Float between 0 and 1.
    - B = Blink, 0 for closed and 1 for open.
Note: If a space is sent instead of data that parameter will be ignored.
- **web_Contoller.html:**
This is a simple webpage that allows for testing the Gakken eye by clicking in a box to move the eye and adjusting the focus with a slider.
