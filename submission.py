# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:30:52 2019

@author: JORGE EDUARDO
"""

import cv2
#import matplotlib.pyplot as plt

# Points
p1=[]
p2=[]

def cut_img(action, x, y, flags, userdata):
  # Referencing global variables 
  global p1, p2
  
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:
      # Save first point
      p1=[(x,y)]
      
      #cv2.putText(img, "x =" + str(p1[0][0]) + "y =" + str(p1[0][1]), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255,255,255), 2 )

  # Action to be taken when left mouse button is released
  elif action==cv2.EVENT_LBUTTONUP:
      # Save Second point
      p2=[(x,y)]
      
      #cv2.putText(img, "x =" + str(p2[0][0]) + "y =" + str(p2[0][1]), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255,255,255), 2 )
      
      # Draw the square
      cv2.rectangle(source, p1[0], p2[0], (255,255,0), 2, cv2.LINE_AA)
      
      cut = img[p1[0][1]:p2[0][1],p1[0][0]:p2[0][0]]
      
      # Draw the circle
      cv2.imwrite("face.jpg",cut)

#################################################################################################################################

img = cv2.imread("sample.jpg",1)

dummy = img.copy()

cv2.namedWindow("Window")

# highgui function called when mouse events occur
cv2.setMouseCallback("Window", cut_img)

k = 0
# loop until "ESC" character is pressed
while k!=27 :
    cv2.imshow("Window", img)
    
    text = '''Choose top left corner, and drag,?'''
    
    cv2.putText(img, text , (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255), 2 );
    
    k = cv2.waitKey(20) & 0xFF
    
    # Another way of cloning
    if k==99:
    	img= dummy.copy()

cv2.destroyAllWindows()
