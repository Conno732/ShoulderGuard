from itertools import count
import face_recognition
import cv2
import numpy as np
import os

def is_blurry(image, thres=120):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #print(cv2.Laplacian(gray, cv2.CV_64F).var())
    return cv2.Laplacian(gray, cv2.CV_64F).var() < thres

def count_faces(image):
    if is_blurry(image): return -1
    face_locs = face_recognition.face_locations(image)
    return len(face_locs)

if __name__ == "__main__":
    '''
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        cv2.putText(frame, str(count_faces(frame)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 3)
        
        cv2.imshow('ShoulderGuard', cv2.resize(frame, (1200, 1200)))
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    vid.release()
    cv2.destroyAllWindows()
    '''

    image = cv2.imread("sample.png")
    print(count_faces(image))