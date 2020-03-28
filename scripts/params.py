from numpy import load

# Pre-captured Contours
h_cnt = load('../Contours/H_contour.npy')
s_cnt = load('../Contours/S_contour.npy')
u_cnt = load('../Contours/U_contour.npy')
# Test Data location
img_dir = '../test data'
# Open cv threshold values for making a binary from gray scaled picture
cv_lower_thr = 80
cv_upper_thr = 255
# Height and Width of scaled Contour
scaled_cnt_coef = 100
# Minimum and Maximum area for a letter Contour
area_lower_bound = 200
area_upper_bound = 2000
""" Matching Algorithm l3 in cvMatchModes
    For more information visit:
    https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html#gaf2b97a230b51856d09a2d934b78c015f
"""
match_alg = 3
# Matching Threshold
match_thr = 1.4