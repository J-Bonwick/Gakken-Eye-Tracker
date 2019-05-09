#!/usr/bin/python
import time
#import tracker
import eye
import threading

#start motion tracker in a new thread
# trackerThread = threading.Thread(target=tracker.track)
# trackerThread.start()

mainLoopThread = threading.Thread(target=mainLoop)
mainLoopThread.start()
def mainLoop():
    eye.autoMove = True
    while True:
        eye.destX = 1
        eye.destY = -1
        #print("X: " + str(tracker.xPos) + ", Y: " + str(tracker.yPos))
eye.init()