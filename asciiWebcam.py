import time
import sys
import pywhatkit
import cv2

def update_text(text):
    sys.stdout.write('\r{}'.format(text))
    sys.stdout.flush()
    
ASCII_CHARS = ["@", "#", "＄", "%", "?", "*", "+", ";", ":", ",", "."]

cam = cv2.VideoCapture(0)
while True:
    ret,frame = cam.read()
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False:
        break
    cv2.imwrite('frame.jpg',frame)
    update_text(pywhatkit.image_to_ascii_art('frame.jpg'))
    key = cv2.waitKey(1)
    if key == ord('q'):
        break



