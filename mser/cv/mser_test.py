# 第一个
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:/codes/ticket.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mser = cv2.MSER_create(_min_area=300)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
regions, boxes = mser.detectRegions(gray)

for box in boxes:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

plt.imshow(img, 'brg')

# 第二个
import cv2
import numpy as np
#Create MSER object
mser = cv2.MSER_create()

#Your image path i-e receipt path
img = cv2.imread('/home/rafiullah/PycharmProjects/python-ocr-master/receipts/73.jpg')

#Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()

#detect regions in gray scale image
regions, _ = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))
cv2.imshow('img', vis)
cv2.waitKey(0)

mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)
for contour in hulls:
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

#this is used to find only text regions, remaining are ignored
text_only = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("text only", text_only)
cv2.waitKey(0)