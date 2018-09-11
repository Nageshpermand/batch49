import cv2


def generate_dataset(img, id, img_id):
    
    cv2.imwrite("data/user."+str(id)+"."+str(img_id)+".jpg", img)

# this is for to draw boundary around the detected feature
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []
    # drawing rectangle around the feature and labeling it
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]
    return coords

# Method to detect the features
def detect(img, faceCascade, eyecascade, noseCascade, mouthCascade):
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Nag")
     
    if len(coords)==4:
        
        roi_img = img[coords[1]:coords[1]+coords[3], coords[0]:coords[0]+coords[2]]
        coords=draw_boundary(roi_img, eyecascade, 1.1, 14, color['red'],"eyes")
        coords=draw_boundary(roi_img, noseCascade, 1.1, 4, color['green'],"nose")
        coords=draw_boundary(roi_img, mouthCascade, 1.1, 20, color['white'],"mouth")
       
        
    return img



faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
noseCascade = cv2.CascadeClassifier('Nariz.xml')
mouthCascade = cv2.CascadeClassifier('Mouth.xml')




video_capture = cv2.VideoCapture(-1)

# Initialize img_id with 0
img_id = 0

while True:
    if img_id % 50 == 0:
        print("Collected ", img_id," images")
    # Reading image from video stream
    _, img = video_capture.read()
    
    img = detect(img, faceCascade, eyesCascade, noseCascade, mouthCascade)
    
    cv2.imshow("face detection", img)
    img_id += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()


