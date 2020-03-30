""" This Code is an Example of finding H U and S letters in Pictures
"""
import cv2 as cv
from contours import find_HSU, img_dir, verbose
import os
import sys


def main(verbose=verbose):
    for filename in os.listdir(img_dir):
        if filename.endswith(".jpg"):
            img = cv.imread(os.path.join(img_dir, filename))
            if verbose:
                print('Analysing pic {} ...'.format(filename))
            letter, center = find_HSU(img, verbose)
            if verbose:
                print('         ... Pic {0} contains {1} letter'.format(filename, letter))
                print('         ... Pic {0} letter location is {1}'.format(filename, center))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2 and sys.argv[1].lower() in ['true', 'false']:
        main(eval(sys.argv[1].upper()[0]+sys.argv[1].lower()[1:]))
    else:
        raise ValueError('Expect a True or False but but something else is passed as input')

