import cv2 as cv
import numpy as np
import pytesseract
from PIL import Image

#functions

def noiseRemoval(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv.erode(image, kernel, iterations=1)
    image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
    image = cv.medianBlur(image, 3)
    return (image)

def grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


#code

# read image
img = cv.imread("letter.jpg")

#resize Image
# print('Original dimensions : ', img.shape)
scale_percent = 20 #percent of original percentage
width = int(img.shape[1] * scale_percent/100)
height = int(img.shape[0] * scale_percent/100)

dim = (width, height)

img_resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
# img_resized = cv.resize()

#make copy of Image
img_copy = np.copy(img_resized)

#make grayscale
img_copy = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)

#invert Image
img_copy = cv.bitwise_not(img_copy)

#make black and white
thresh, im_bw = cv.threshold(img_copy, 180, 255, cv.THRESH_BINARY)
ocr_result = pytesseract.image_to_string(im_bw)


#noise removal
# im_bw = noiseRemoval(im_bw)

cv.imshow("Image", im_bw)
print(ocr_result)
# print(img_resized.shape)

cv.waitKey(0)
