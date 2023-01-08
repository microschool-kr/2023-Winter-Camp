import cv2
import os

path = os.path.abspath(os.path.dirname(__file__))

# 동영상을 받아올 카메라 선언 및 설정 (0인덱스가 내장 카메라, 1이 웹캠)
capture = cv2.VideoCapture(0) 
# 영상 가로, 세로 사이즈 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
fps = capture.get(cv2.CAP_PROP_FPS)
dt = int(1000/fps)
n = 1
# 무한반복문
while True:
    _, frame = capture.read()     # 카메라로부터 현재 영상을 받아 frame에 저장
    cv2.imshow("cam", frame)        # frame(카메라 영상)을 cam 이라는 창에 띄워줌

    key = cv2.waitKey(dt) & 0xFF
    
    if key == ord('q'):  # 키보드의 q 를 누르면 종료
        break
    
    if key == ord('p'):  # p 누르면 프레임 캡쳐
        file_name = f"capture{n}.jpg"
        img_file = os.path.join(path, file_name)
        cv2.imwrite(img_file, frame) # 현제 폴더에 capure01.jpg로 이미지 저장
        print("Image captured.")    #캠쳐 되었다고 프린트
        n += 1

capture.release()                   # 캡처 객체를 없앰
cv2.destroyAllWindows()             # 모든 창 닫음
