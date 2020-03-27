""" This is an example code for generating new contours"""
import numpy as np
import cv2 as cv
from numpy import save
import contours

img = cv.imread('../test data/a.jpg')
cnt, center = contours.find_contour(img)

cv.drawContours(img, [cnt], 0 , (0,255,0),1)

save('../Contours/H_contour.npy',cnt)
cv.imshow('result', img)

cv.waitKey()