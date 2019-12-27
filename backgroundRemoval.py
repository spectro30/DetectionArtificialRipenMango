import cv2
import numpy as np


defaultImageTag = "Image"



def resizeImage(img):
    widthPixel = 540
    aspectRatio = img.shape[0] / img.shape[1]
    dimension = (widthPixel, int(aspectRatio * widthPixel))
    resImg = cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)
    return resImg

def filterImage(img):
    return cv2.medianBlur(img, 5)

def displayImage(img, imageTag):
    cv2.imshow(imageTag, img)
    cv2.waitKey(0)

def thresholdImage(img, windowSize):
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
     cv2.THRESH_BINARY, 11, windowSize)



img = cv2.imread('sample1.jpg',0)

displayImage(backgroundSubstraction(img), defaultImageTag)

