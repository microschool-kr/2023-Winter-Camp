import cv2
import os

path = os.path.abspath(os.path.dirname(__file__))
file_name = "shapes.png"
img_file = os.path.join(path, file_name)
print(img_file)

# RGB 이미지 데이터
img = cv2.imread(img_file)


# B : 0 ~ 150, G : 0 ~ 150, R : 100 ~ 255
dst1 = cv2.inRange(img, (0, 0, 100), (150, 150, 255))

filtered_image = cv2.bitwise_and(img, img, mask=dst1)


cv2.imshow("color", img)
cv2.imshow("mask", dst1)
cv2.imshow("red", filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
