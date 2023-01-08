import cv2
import os
import sys

path = os.path.abspath(os.path.dirname(__file__))
file_name = "haarcascade_frontalface_default.xml"
cascade_file = os.path.join(path, file_name)

# Cascade Classifier 선언
face_cascade = cv2.CascadeClassifier(cascade_file)


# 동영상을 받아올 카메라 선언 및 설정 (0인덱스가 내장 카메라, 1이 웹캠)
capture = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Fail to open camera!")
    sys.exit()

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
fps = capture.get(cv2.CAP_PROP_FPS)
dt = int(1000/fps)

while True:
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    if len(faces):
        for (x, y, w, h) in faces:
            face_rectangle = cv2.rectangle(
                frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            Face_text = cv2.putText(img=face_rectangle,
                                    text="Face",
                                    org=(x, y+h+30),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1, color=(0, 0, 255),
                                    thickness=2, lineType=cv2.LINE_4)

            print("Face")

    cv2.imshow("cam", frame)

    if cv2.waitKey(dt) & 0xFF == ord('q'):
        break
        
capture.release()
cv2.destroyAllWindows()
