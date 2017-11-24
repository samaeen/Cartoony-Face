 #import necessary modules
import pygame
import cv2
import numpy as np

#load cascades
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)

#initialize pygame
pygame.init()

#initialaize display size variables
displayWidth=800
displayHeight=600

#initialize game colors
white=(255,255,255)

gameDisplay=pygame.display.set_mode((displayWidth,displayHeight))	#display game window
pygame.display.set_caption('Watching U')							#game display caption
clock=pygame.time.Clock()											#pygame's time to initialize times for events
eyeBall=pygame.image.load('eyeBalls.jpg')							#load image

#function to show image
def eyeBallFunc(x,z):
	gameDisplay.blit(eyeBall,(x,z))

#setting x,y for first eyeball,x2,y2 for second eyeball position
x=(displayWidth*0.30)
z=(displayHeight*0.40)


crashed=False														#total game in a boolean crashed 


#main game loop
while not crashed:
	ret,img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.6,5)
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:								#if quit is pressed game crashed :P 
			crashed=True

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray=gray[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]
		eyes=eye_cascade.detectMultiScale(roi_gray)
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
			#print('start point ',ex,'end point',ex+ew)
	cv2.imshow('img',img)
	gameDisplay.fill(white)
	eyeBallFunc(x,z)
	pygame.display.update()
	clock.tick(60)

cap.release()
cv2.destroyAllWindows()
pygame.quit()
quit()
