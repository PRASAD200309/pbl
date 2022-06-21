#import cv2 for image recognition and identification
import cv2
#import pyplot to create rectangle
from matplotlib import pyplot
#import numpy to do mathermatical operation on array
import numpy as np

#import image and resize
img=cv2.imread('image.jpg')
img=cv2.resize(img,(400,600))

#convert image to greyscale
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_rgb=np.copy(imgGray)
img1=cv2.resize(img_rgb,(400,600))

#point to locate min and max point of the array
point=cv2.minMaxLoc(img1)

#to locate the coordinates of the brightest point
max_loc_x= cv2.minMaxLoc(img1)[3][0]
max_loc_y= cv2.minMaxLoc(img1)[3][1]
print(max_loc_x)
print(max_loc_y)

#to plot the rectangle
s=25
coord1=(max_loc_x-s,max_loc_y-s)
coord2=(max_loc_x+s,max_loc_y+s)
center_coordinates=(max_loc_x,max_loc_y)
color=(255,0,0)
t=5

#to show the final position of the brightest spot on the original image
image_box=np.copy(img)
image_box=cv2.rectangle(image_box,coord1,coord2,color,t)
pyplot.imshow(image_box)
cv2.imshow('image',image_box)
cv2.waitKey(0)

'''Output 
coordinates of the brightest point are:
x = 210
y = 347
'''