# Gakken-Eye-Tracker
Projects an eye onto the gakken Worldeye That follows people

## Files:
eye.py - Displays the eye on the display and controls its position.
  Websocket input: `"[gakken]X,Y,IRIS,BLINK"`. X,Y and iris are floating point values between 0 and 1. Blink is yet to implemented.
 
web_Contoller.html - Simple html page that allows basic control of the eye.
