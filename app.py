import cv2
import numpy as np
defaultImageTag = "Queen"

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


def backgroundSubstraction(img):
    
    #parameters
    BLUR = 21
    CANNY_THRESH_1 = 10
    CANNY_THRESH_2 = 100
    MASK_DILATE_ITER = 10
    MASK_ERODE_ITER = 10
    #Ends Here

    #Edge Detection
    img = resizeImage(img)
    edges = cv2.Canny(img, CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)
    #Ends Here
    
    #Find Max Contour
    maxContourArea = 0
    contour_info = []
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        contour_info.append( (c, cv2.isContourConvex(c), cv2.contourArea(c),))
        maxContourArea = max(maxContourArea, cv2.contourArea(c))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
    max_contour = contour_info[0]
    print(maxContourArea)
    #Ends Here

    #Create and Apply the mask
    mask = np.zeros(edges.shape)
    cv2.fillConvexPoly(mask, max_contour[0], (255))
    r, c = img.shape[0], img.shape[1]
    for i in range(r):
        for j in range(c):
            if not mask[i][j]:
                img[i][j] = 255
    #Ends Here

    return img

def totalBlackPix(img):
    img = cv2.imread('003.png',0)
    r, c = img.shape[0], img.shape[1]
    ans = 0
    for i in range(r):
        for j in range(c):
            if not img[i][j]:
                ans += 1
    
    print (ans)



img = cv2.imread('testData/sample20.jpg',0)
img = resizeImage(img)
img = filterImage(img)
img = backgroundSubstraction(img)
img = thresholdImage(img, 3)
img = totalBlackPix(img)



#displayImage(img, 'image')

