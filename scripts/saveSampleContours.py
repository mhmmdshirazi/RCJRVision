""" This is an example code for generating new contours"""
import cv2 as cv
from numpy import save
import contours

# Read a sample image from file
img = cv.imread('../test data/u.jpg')
# Find Image Contour
cnt, center = contours.find_contour(img, verbose=False)
# Save sample Contour to a .npy file
save('../Contours/U_contour.npy', cnt)
# Draw and show sample Contour
cv.drawContours(img, [cnt], 0, (0, 255, 0), 1)
cv.imshow('result', img)
cv.waitKey()
