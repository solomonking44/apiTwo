import cv2 as cv
import numpy as np
import pytesseract
from PIL import Image

# functions

# def noiseRemoval(image):
#     kernel = np.ones((1, 1), np.uint8)
#     image = cv.dilate(image, kernel, iterations=1)
#     kernel = np.ones((1, 1), np.uint8)
#     image = cv.erode(image, kernel, iterations=1)
#     image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
#     image = cv.medianBlur(image, 3)
#     return (image)


def grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


# code

# read image
img = cv.imread("letter.jpg")

# resize Image
# print('Original dimensions : ', img.shape)
scale_percent = 20  # percent of original percentage
width = int(img.shape[1] * scale_percent/100)
height = int(img.shape[0] * scale_percent/100)

dim = (width, height)

img_resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
# img_resized = cv.resize()

# make copy of Image
img_copy = np.copy(img_resized)

# make grayscale
img_copy = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)

# invert Image
img_copy = cv.bitwise_not(img_copy)

# make black and white
thresh, im_bw = cv.threshold(img_copy, 180, 255, cv.THRESH_BINARY)

# find bold text
# thresh1, im_bw1 = cv.threshold(img_copy, 230, 255, cv.THRESH_BINARY)

# get text from image using tesseract
# ocr_result = pytesseract.image_to_string(im_bw)
# adaptive thresholding
# adaptive_threshold = cv.adaptiveThreshold(
# img_copy, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 2)

# image to get bold text
bold_text = pytesseract.image_to_string(im_bw)


# noise removal
im_noise = cv.fastNlMeansDenoising(im_bw, None, 8, 7, 21)


# show image
cv.imshow("Adaptive Threshold", im_noise)
# print(ocr_result)
print(bold_text)
# print(img_resized.shape)

cv.waitKey(0)
