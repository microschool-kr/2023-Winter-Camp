import cv2
import os

path = os.path.abspath(os.path.dirname(__file__))
file_name = "shapes.png"
img_file = os.path.join(path, file_name)

# 이미지를 읽어서 그레이 스케일 및 스레시홀드 변환
img = cv2.imread(img_file)
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)

# 컨투어 찾기
# *RETR_EXTERNAL=가장 바깥쪽 컨투어만 담아서 반환
# *CHAINN_APPROX_SIMPLE = 직선을 구성하는 모든 점의 좌표를 얻는게 아니라, 양 끝의 좌표만 저장
# [-2:] last two items in the array
contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)[-2:]

for contour in contours:
    # 각 컨투어에 근사 컨투어로 단순화 (삐쭉 삐쭉 나온 부분 무시)
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    # 꼭지점의 갯수
    vertices = len(approx)
    

    # 중심점 찾기
    mmt = cv2.moments(contour)
    if mmt['m00'] == 0:
        print("")
    else:
        cx, cy = int(mmt['m10']/mmt['m00']), int(mmt['m01']/mmt['m00'])

    name = "Unkown"
    if vertices == 3:  # 꼭지점이 3개는 삼각형
        name = "Triangle"
        color = (0, 255, 0)
    elif vertices == 4:  # 꼭지점 4개는 사각형
        x, y, w, h = cv2.boundingRect(contour)
        if abs(w-h) <= 3:   # 폭과 높이의 차이가 3보다 작으면 정사각형
            name = "Square"
            color = (0, 125, 255)
        else:               # 폭과 높이 차이가 3보다 크면 직사각형
            name = "Rectangle"
            color = (0, 0, 255)
    elif vertices == 5:  # 꼭 지점 갯수 6개는 팔각형형
        name = "Pentagon"
        color = (255, 255, 0)
    elif vertices == 6:  # 꼭 지점 갯수 6개는 팔각형형
        name = "Hexagon"
        color = (255, 255, 0)
    elif vertices >= 15:  # 꼭 지점 10개 이상이면 원
        name = "Circle"
        color = (0, 255, 255)

    # 컨투어 그리기
    cv2.drawContours(img2, [contour], -1, (0, 255, 0), 3)
    # 도형 이름 출력
    cv2.putText(img2, name, (cx-50, cy), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1, (255, 255, 255), 1)

cv2.imshow("Input Shapes", img)
cv2.imshow("Recognizing Shapes", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
