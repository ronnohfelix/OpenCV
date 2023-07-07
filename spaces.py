import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/wolf.jpg')
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# BGR to Grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(resized, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b', lab)

# BGR to RGB
rgb = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)