import cv2 as cv
import numpy as np

img = cv.imread('Photos/bird.jpg')
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Averaging
average = cv.blur(resized, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(resized, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(resized, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(resized, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)