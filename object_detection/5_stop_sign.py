import cv2
import os

path = os.path.abspath(os.path.dirname(__file__))
file_name = "cascade_stop_sign.xml"
cascade_file = os.path.join(path, file_name)
print(path)

# Cascade Classifier xml
stop_sign = cv2.CascadeClassifier(cascade_file)

# 동영상을 받아올 카메라 선언 및 설정 (0인덱스가 내장 카메라, 1이 웹캠)
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
fps = capture.get(cv2.CAP_PROP_FPS)
dt = int(1000/fps)

while True:
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)

    # Detect the stop sign, x,y = origin points, w = width, h = height
    if len(stop_sign_scaled):
        for (x, y, w, h) in stop_sign_scaled:
            # Draw rectangle around the stop sign
            stop_sign_rectangle = cv2.rectangle(frame, (x, y),
                                                (x+w, y+h),
                                                (0, 255, 0), 3)
            # Write "Stop sign" on the bottom of the rectangle
            stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                         text="Stop Sign",
                                         org=(x, y+h+30),
                                         fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                         fontScale=1, color=(0, 0, 255),
                                         thickness=2, lineType=cv2.LINE_4)
            print("Stop Sign")

            
    cv2.imshow("cam", frame)

    
    if cv2.waitKey(dt) & 0xFF == ord('q'):
        break
        
capture.release()
cv2.destroyAllWindows()
