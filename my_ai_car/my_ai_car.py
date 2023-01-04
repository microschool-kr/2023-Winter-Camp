import serial
import cv2
import tensorflow.keras
import numpy as np
import os

def main():
    ser = serial.Serial("COM3", baudrate=9600)
    
    path = os.path.abspath(os.path.dirname(__file__))
    filename = "keras_model.h5"
    label = []
    with open(os.path.join(path, "labels.txt")) as f:
        for line in f.readlines():
            label.append(line.split()[1].strip())

    model = tensorflow.keras.models.load_model(os.path.join(path, filename))

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Fail to open camera!")
        return True

    fps = cap.get(cv2.CAP_PROP_FPS)
    dt = int(1000/fps)


    while True:
        ret, frame = cap.read()
        if not ret:
            ret, frame = cap.read()
            if not ret:
                print("Fail to read frame!")
                break

        frame_resized = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1
        frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))

        prediction = model.predict(frame_reshaped)
        idx = np.where(prediction[0] == max(prediction[0]))[0][0]

        cv2.putText(
            frame,
            f"{label[idx].upper()}!!",
            (13, 230),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0, 255, 0),
            4,
        )

        cv2.imshow("frame", frame)
        if idx == 0:
            ser.write(b'0')
        else:
            ser.write(b'2')
        print(idx)

        if cv2.waitKey(dt) & 0xFF == 27:
            ser.write(b'0')
            print("end")
            break
    
    cv2.destroyAllWindows()
    cap.release()
    ser.close()

if __name__ == "__main__":
    main()
