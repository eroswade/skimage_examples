import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

mser = cv2.MSER_create()

kp1, des1 = mser.detect(img1)
kp2, des2 = mser.detect(img2)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.8 * n.distance:
        good.append(m)

good = sorted(good, key=lambda x: x.distance)

matching_result = cv2.drawMatches(img1, kp1, img2, kp2, good, None, flags=2)
cv2.imwrite('result.jpg', matching_result)