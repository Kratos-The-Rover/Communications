import numpy as np 
import cv2
#cap = cv2.VideoCapture('test.mp4')
cap = cv2.VideoCapture('test.mp4')

def change_res(width, height):
	cap.set(3,width)
	cap.set(4, height)

def lowest_res():
	cap.set(3, 640)
	cap.set(4, 480)

def highest_res():
	cap.set(3,1920)
	cap.set(4, 1080)

def resize_frame(frame, percent):
    width = int(frame.shape[1]*percent/100)
    height = int(frame.shape[0]*percent/100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

lowest_res()

while(True):
	ret, frame = cap.read()
	#frame = resize_frame(frame, percent = 50)
	cv2.imshow('frame', frame)
	#frame2 = resize_frame(frame, percent = 1000)
	#cv2.imshow('frame2', frame2)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break


cap.release()
cap.destroyAllWindows()

