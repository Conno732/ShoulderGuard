from itertools import count
import face_recognition
import cv2
import numpy as np
import os
    
def is_blurry(image, thres=120):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #print(cv2.Laplacian(gray, cv2.CV_64F).var())
    return cv2.Laplacian(gray, cv2.CV_64F).var() < thres


def register(save_filename="user.npy", num_encodings=30):
    vid = cv2.VideoCapture(0)
    face_encodings = []
    while True:
        ret, frame = vid.read()
        
        if is_blurry(frame): 
            cv2.putText(frame, "The camera is blurry", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,139), 3)
        else:
            face_locs = face_recognition.face_locations(frame)
            if len(face_locs) == 0: 
                cv2.putText(frame, "There is no one in the camera.", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,139), 3)
            elif len(face_locs) > 1:
                cv2.putText(frame, "Multiple people are in the camera.", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,139), 3)
            else:
                top, right, bottom, left = face_locs[0]
                face_area_ratio = (top - bottom)*(left-right)/ (frame.shape[0] * frame.shape[1])
                
                print(top, right, bottom, left)
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                print(face_area_ratio)
                if face_area_ratio < 0.16:
                    cv2.putText(frame, "Please put your face closer the camera.", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,139), 3)
                else:
                    cv2.putText(frame, "Valid face. Hold still!", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,100,0), 3)
                    face_encodings.append(face_recognition.face_encodings(frame)[0])
                    if len(face_encodings) == num_encodings: 
                        face_encodings = np.array(face_encodings)
                        with open(save_filename, "wb") as f:
                            np.save(f, face_encodings)
                        break

        cv2.imshow('ShoulderGuard Registration', cv2.resize(frame, (1200, 1200)))
    
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    vid.release()
    cv2.destroyAllWindows()

    print("Registration completed!")

def detect(save_filename="user.npy"):
    if not os.path.isfile(save_filename):
        print("You probably have not registered yet.")
        return 

    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        if is_blurry(frame): 
            cv2.putText(frame, "The camera is blurry", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,139), 3)
        else:
            face_locs = face_recognition.face_locations(frame)
            if len(face_locs) == 0: 
                cv2.putText(frame, "There is no one in the camera.", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,139), 3)
            elif len(face_locs) > 1:
                cv2.putText(frame, "Multiple people are in the camera.", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,139), 3)
            else:
                top, right, bottom, left = face_locs[0]
                #print("ratio", face_area_ratio)
                
                unknown_encoding = face_recognition.face_encodings(frame)[0]
                with open(save_filename, "rb") as f:
                    user_face_encodings = np.load(f)
                encoding_dist = np.average(face_recognition.face_distance(user_face_encodings, unknown_encoding))
                
                if encoding_dist < 0.55:
                    cv2.putText(frame, "Correct face!", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,100,0), 3)
                else:
                    cv2.putText(frame, "Wrong face!", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,139), 3)
         
        cv2.imshow('ShoulderGuard Detection', cv2.resize(frame, (1200, 1200)))
    
        if cv2.waitKey(1) & 0xFF == ord('q'): break

if __name__ == "__main__":
    detect()
