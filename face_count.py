from itertools import count
import face_recognition
import cv2
import numpy as np
import base64

def is_blurry(image, thres=120):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #print(cv2.Laplacian(gray, cv2.CV_64F).var())
    return cv2.Laplacian(gray, cv2.CV_64F).var() < thres

def base64_to_image(b64_data):
    #nparr = np.frombuffer(base64.b64decode(b64_data + "="), dtype=np.uint8)
    #print(nparr.shape)
    #print(cv2.imdecode(nparr,-1))
    header, data = b64_data.split(',', 1)
    image_data = base64.b64decode(data)
    nparr = np.frombuffer(image_data, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
def count_faces(image):
    print(is_blurry(image))
    #if is_blurry(image): return -1
    face_locs = face_recognition.face_locations(image,model="cnn")
    for  top, right, bottom, left in face_locs:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.imwrite("sample_out.png", image)
    return len(face_locs)

def check_image(b64_data):
    return count_faces(base64_to_image(b64_data)) > 1
    

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

    #image = cv2.imread("sample.png")
    #print(count_faces(image))  
    with open("message.txt", "r") as f:
        #print(f.read())
        img = base64_to_image(f.read())
        print(count_faces(img))
        cv2.imshow("image", img)
        cv2.waitKey(0)