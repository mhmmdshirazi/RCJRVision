""" This Code is an Example of finding H U and S letters in Pictures
"""
from numpy import load
import cv2 as cv
from contours import *
import time
import os

# Load contours
h_cnt = load('../Contours/H_contour.npy')
s_cnt = load('../Contours/S_contour.npy')
u_cnt = load('../Contours/U_contour.npy')
img_dir = '../test data'
# test method using
for filename in os.listdir(img_dir):
    if filename.endswith(".jpg"):
        img = cv.imread(os.path.join(img_dir, filename))
        print('Analysing pic {} ...'.format(filename))
        letter, center = find_HSU(img, h_cnt, s_cnt, u_cnt)
        print('         ... Pic {0} contains {1} letter'.format(filename, letter))

# img = cv.imread('../test data/u5.jpg')
# start = time.time()
# letter, center = contours.find_HSU(img, h_cnt, s_cnt, u_cnt)
# end = time.time()
# print(letter)
# if letter is None:
#     print('There is no letter in this pic')
# else:
#     print('This pic has {} letter'.format(letter))
#     print('The Location of Center is:', center)
