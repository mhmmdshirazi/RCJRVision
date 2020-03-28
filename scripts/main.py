""" This Code is an Example of finding H U and S letters in Pictures
"""
import cv2 as cv
from contours import find_HSU, img_dir
import os

# test method using
for filename in os.listdir(img_dir):
    if filename.endswith(".jpg"):
        img = cv.imread(os.path.join(img_dir, filename))
        print('Analysing pic {} ...'.format(filename))
        letter, center = find_HSU(img)
        print('         ... Pic {0} contains {1} letter'.format(filename, letter))
        print('         ... Pic {0} letter location is {1}'.format(filename, center))
