import numpy as np
import cv2 as cv
from params import *


# Finding the letter contour in the picture
def find_contour(img, verbose):
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, cv_lower_thr, cv_upper_thr, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # Return None if there is no contour in picture
    if len(contours) == 0:
        return None, None
    areas = [cv.contourArea(cnt) for cnt in contours]
    if verbose:
        print('         ... Containing areas are:', areas)
    if not np.any(np.logical_and(np.array(areas) < area_upper_bound, np.array(areas) > area_lower_bound)):
        return None, None

    cnt = contours[np.argmin(areas)]
    x, y, w, h = cv.boundingRect(cnt)
    center = [x + w / 2, y + h / 2]
    shifted_cnt = cnt - [x, y]
    scaled_cnt = shifted_cnt
    scaled_cnt[:, :, 0] = np.uint(shifted_cnt[:, :, 0] * scaled_cnt_coef / w)
    scaled_cnt[:, :, 1] = np.uint(shifted_cnt[:, :, 1] * scaled_cnt_coef / h)
    return scaled_cnt, center


# Find difference of contours
def find_diff(cnt1, cnt2):
    return cv.matchShapes(cnt1, cnt2, match_alg, 0)


# Find the HSU Letter in contuor
def find_HSU(img, verbose):
    contour, center = find_contour(img, verbose)
    if contour is None:
        return None, None
    h_diff = find_diff(contour, h_cnt)
    s_diff = find_diff(contour, s_cnt)
    u_diff = find_diff(contour, u_cnt)
    min_diff = min([h_diff, s_diff, u_diff])
    diff_arg = np.argmin([h_diff, s_diff, u_diff])
    # debug
    # cv.drawContours(img,[h_cnt],0,(0,255,0),1)
    # cv.drawContours(img, [contour], 0, (0, 0, 255), 1)
    # cv.imshow('c',img)
    # cv.waitKey()
    if verbose:
        print('         ... diff to ref is:', min_diff)
    if min_diff > match_thr:
        return None, None
    if diff_arg == 0:
        return 'H', center
    elif diff_arg == 1:
        return 'S', center
    else:
        return 'U', center
