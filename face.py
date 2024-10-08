import cv2


face_cascade = cv2.CascadeClassifier(r'C:\Users\arunp\Downloads\abhi\working\haarcascade_frontalface_default.xml')


img = cv2.imread(r'C:\Users\arunp\Downloads\abhi\working\community-concept-with-group-people.jpg')


if img is None:
    print("Error loading image")
else:
    
    img = cv2.resize(img, (800, 600))  

   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

  
    if len(faces) == 0:
        print("No faces found")
    else:
      
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

   
    cv2.imshow('img', img)
    
    
    cv2.waitKey(0)  


cv2.destroyAllWindows()
