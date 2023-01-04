import cv2
import os

path = os.path.abspath(os.path.dirname(__file__))
file_name = "cat.jpeg"
img_file = os.path.join(path, file_name)

# 이미지 데이터를 img라는 변수에 저장
img = cv2.imread(img_file)

if img is not None: # 이미지파일 있으면 아래 실행
    # 이미지 데이터 프린트
    print(img)

    # 이미지를 흑백으로 전환하고, img_gray라는 변수에 저장
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('original', img)     # 원본 이미지 보이기
    cv2.imshow('gray', img_gray)    # 흑백 이미지 보이기
    
    cv2.waitKey()                   # 사용자 키 입력시 까지 기다리기
    cv2.destroyAllWindows()         # 모든 창 종료

else: # 이미지가 없으면 에러 메세지 출력
    print('No image file.')
