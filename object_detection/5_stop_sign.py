import cv2
import os

path = os.path.abspath(os.path.dirname(__file__))
file_name = "cascade_stop_sign.xml"
cascade_file = os.path.join(path, file_name)
print(path)

# Cascade Classifier xml
stop_sign = cv2.CascadeClassifier(cascade_file)

# 내장 카메라가 인덱스 0, USB로 연결한 웹캠은 인덱스 1로 하면 됩니다
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)

    # Detect the stop sign, x,y = origin points, w = width, h = height
    if len(stop_sign_scaled):
        for (x, y, w, h) in stop_sign_scaled:
            # Draw rectangle around the stop sign
            stop_sign_rectangle = cv2.rectangle(img, (x, y),
                                                (x+w, y+h),
                                                (0, 255, 0), 3)
            # Write "Stop sign" on the bottom of the rectangle
            stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                         text="Stop Sign",
                                         org=(x, y+h+30),
                                         fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                         fontScale=1, color=(0, 0, 255),
                                         thickness=2, lineType=cv2.LINE_4)
            # send string to arduino
            print(f"Stop Sign")
            # ser.write("1".encode())
            is_stop = True

    cv2.imshow("img", img)

    key = cv2.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
