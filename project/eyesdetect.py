# open cv2 is computer vision open sourse library files are available
# this is for face and eyes detection
import cv2

# Method to generate dataset to recognize a human face
def generate_dataset(img, id, img_id):
     # write image in data direction
    cv2.imwrite("data/user.%s"%(id)+"."%(img_id)+".jpg", img)

# this is for to draw boundary 
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    # Converting image to gray-scale (grayscale image contains only shades of gray and no color)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # detecting features in gray-scale image, returns coordinates, width and height of features
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []

    # drawing rectangle around the feature and labeling it
    for (x, y, w, h) in features:
       cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
       cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1,  )
       coords = [x, y, w, h]
    #Coordinates are a set of values thatshowan exact position.On graphs it iscommon to have a pairofnumbers to show

    return coords




# Method to detect the features  and (255,0,0)and(0,0,255) rgb values
def detect(img, faceCascade, eyecascade):
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['green'], "Nag")
    

     #If feature is detected, the draw_boundary method will returnthe x,y coordinatesand width andheight of rectangle
                
    if len(coords)==4:
        
         # Updating region by cropping image
         #roi_img = a region of intrest which is a binary img that is the same size as the image want to process
         # and roi img can createROIs ofmany shapes using the high-level ROI functions,such asdrawcircle ordrawpolygon
        roi_img = img[coords[1]:coords[1]+coords[3], coords[0]:coords[0]+coords[2]]
                # Assign unique id to each user

        coords=draw_boundary(roi_img, eyecascade, 1.1, 14, color['red'],"eyes")
       
        
    return img


# Loading classifiers facecascade and eyescascade
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')





# Capturing real time video stream. 0 for built-in web-cams, 0 or -1 for external web-cams
video_capture = cv2.VideoCapture(0)


img_id = 0

while True:
    if img_id % 50 == 0:
        print("Collected ", img_id," images")
    # Reading image from video 
    _, img = video_capture.read()
    
    # Call method we defined above
    img = detect(img, faceCascade, eyesCascade)
    
     # Writing processed image in a new window
    cv2.imshow("face detection", img)
    img_id += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releasing  machine-cam
video_capture.release()


