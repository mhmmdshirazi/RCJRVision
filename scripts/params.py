from numpy import load


h_cnt = load('../Contours/H_contour.npy')
s_cnt = load('../Contours/S_contour.npy')
u_cnt = load('../Contours/U_contour.npy')
img_dir = '../test data'

cv_lower_thr = 80
cv_upper_thr = 255

scaled_cnt_coef = 100

area_lower_bound = 200
area_upper_bound = 2000

match_alg = 3
match_thr = 0.4
