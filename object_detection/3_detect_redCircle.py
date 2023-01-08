import numpy as np
import cv2

# 동영상을 받아올 카메라 선언 및 설정 (0인덱스가 내장 카메라, 1이 웹캠)
capture = cv2.VideoCapture(0)
# 영상 가로, 세로 사이즈 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 가로
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 세로
fps = capture.get(cv2.CAP_PROP_FPS)
dt = int(1000/fps)

while True:
    _, frame = capture.read()  # 카메라로부터 현재 영상을 받아 frame에 저장

    # Lab 색상 공간으로 변경, a 채널을 이용하여 빨간색을 찾을 수 있음
    frame_lab = cv2.cvtColor(frame, cv2.COLOR_BGR2Lab)

    # Threshold the Lab image, keep only the red pixels
    # Possible yellow threshold: [20, 110, 170][255, 140, 215]
    # Possible blue threshold: [20, 115, 70][255, 145, 120]

    frame_lab_red = cv2.inRange(frame_lab, np.array([20, 150, 150]),
                                         np.array([190, 255, 255]))
    frame_lab_red = cv2.GaussianBlur(frame_lab_red, (5, 5), 2, 2)
    
    # 이미지에서 원을 찾음
    circles = cv2.HoughCircles(frame_lab_red, cv2.HOUGH_GRADIENT, 1,
                               frame_lab_red.shape[0] / 8, param1=100, param2=18,
                               minRadius=5, maxRadius=60)

    # 찾아낸 원의 테두리를 그림
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2],
                   color=(0, 255, 0), thickness=2)

    cv2.imshow('cam', frame)    # frame(카메라 영상)을 cam 이라는 창에 띄워줌
    if cv2.waitKey(dt) & 0xFF == ord('q'):   # 키보드의 q 를 누르면 종료
        break


capture.release()   # 캡처 객체를 없앰
cv2.destroyAllWindows() # 모든 창 닫음
