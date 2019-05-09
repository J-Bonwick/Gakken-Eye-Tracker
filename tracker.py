# imports 
import os,sys,time 
import numpy as np
import cv2

xPos = 0
yPos = 0

def track():
    global xPos
    global yPos
    camera = cv2.VideoCapture(0)
    camera.set(3,320)
    camera.set(4,240)
    time.sleep(0.5)
    master = None

    while True:
        # grab a frame
        (grabbed,frame0) = camera.read()
        # end of feed
        if not grabbed: break
        # gray frame
        frame1 = cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)
        # blur frame 
        frame2 = cv2.GaussianBlur(frame1,(21,21),0)
        # initialize master
        if master is None:
            master = frame2
            continue
        # delta frame
        frame3 = cv2.absdiff(master,frame2)
        # threshold frame
        frame4 = cv2.threshold(frame3,15,255,cv2.THRESH_BINARY)[1]
        # dilate the thresholded image to fill in holes
        kernel = np.ones((5,5),np.uint8)
        frame5 = cv2.dilate(frame4,kernel,iterations=4)
        # find contours on thresholded image
        contours,nada = cv2.findContours(frame5.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # target contours
        targets = []
        # loop over the contours
        for c in contours:
           # if the contour is too small, ignore it
            if cv2.contourArea(c) < 500:# make sure this has a less than sign, not an html escape 
                continue 
            # contour data
            M = cv2.moments(c)
            x,y,w,h = cv2.boundingRect(c)
            rx = x+int(w/2)
            ry = y+int(h/2)
            ca = cv2.contourArea(c)
            # save target contours
            targets.append((rx,ry,ca))
        # make target
        xPos = 0
        yPos = 0
        if targets:
            for x,y,a in targets:
                xPos += x
                yPos += y
            xPos = int(round(xPos/len(targets),0))
            yPos = int(round(yPos/len(targets),0))
        # update master
        master = frame2
        # key delay and action
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key != 255:
            print('key:',[chr(key)])
    # release camera
    #camera.release()