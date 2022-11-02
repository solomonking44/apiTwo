# open cv
import cv2 as cv

# making a copy of an image
import numpy as np

# reading text from image
import pytesseract

# storing image (in compiler - i think)
img = cv.imread('letter.jpg')

# printing the original dimensions of the image
print(img.shape[0])  # height
print(img.shape[1])  # width

# factor for reducing image size
reduce_by = 20

# new dimensions
new_height = (reduce_by)/100 * img.shape[0]
new_width = (reduce_by)/100 * img.shape[1]

# might be a list or array
dim = (int(new_width), int(new_height))

# making a resized image
img_resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

# making a copy of the image
img_copy = np.copy(img_resized)

# turning the image to grayscale
img_gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)

# reading text from image using tesseract online - An API for this kind of stuff
text_from_image = pytesseract.image_to_string(img_gray)

# PRINT THE TEXT
print(text_from_image)

# just in case you need to compare and contrast
# check the image next to the text
cv.imshow("GRAY IMAGE", img_resized)

# this is so the image appears and stays up
# otherwise it would show up and dissappear again
cv.waitKey(0)

# Thank you, Next!
