import cv2
import os

path = os.path.abspath(os.path.dirname(__file__))
file_name = "haarcascade_frontalface_default.xml"
cascade_file = os.path.join(path, file_name)

# Cascade Classifier xml
face_cascade = cv2.CascadeClassifier(cascade_file)


# 내장 카메라가 인덱스 0, USB로 연결한 웹캠은 인덱스 1로 하면 됩니다
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    is_stop = False

    # Draw the rectangle around each face
    if len(faces):
        for (x, y, w, h) in faces:
            face_rectangle = cv2.rectangle(
                img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            Face_text = cv2.putText(img=face_rectangle,
                                    text="Face",
                                    org=(x, y+h+30),
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                    fontScale=1, color=(0, 0, 255),
                                    thickness=2, lineType=cv2.LINE_4)

            print(f"Face")

    cv2.imshow("img", img)

    key = cv2.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
