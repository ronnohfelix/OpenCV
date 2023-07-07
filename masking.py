import cv2 as cv
import numpy as np

img = cv.imread('Photos/wolf.jpg')
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

blank = np.zeros(resized.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank, (resized.shape[1]//2, resized.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(resized, resized, mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)