""" This Code is an Example of finding H U and S letters in Pictures
"""
from numpy import load
import cv2 as cv
import contours
import time
#Load contours
h_cnt = load('../Contours/H_contour.npy')
s_cnt = load('../Contours/S_contour.npy')
u_cnt = load('../Contours/U_contour.npy')
#test method using
img = cv.imread('../test data/u5.jpg')
start = time.time()
letter, center = contours.find_HSU(img,h_cnt,s_cnt,u_cnt)
end = time.time()
print(letter)
if letter is None:
    print('There is no letter in this pic')
else:
    print('This pic has {} letter'.format(letter))
    print('The Location of Center is:', center)
