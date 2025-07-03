import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

if not cap.isOpened():
    print("Could not open camera, pleaase try again...")
    exit()

while True:
    ret ,image=cap.read()

    if not ret:
        print("failed to capture")
        break



    gray=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x,y, w, h) in face:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 206, 124), 2)

    cv2.imshow("face detection", image)

    if cv2.waitKey(1) and 0xFF==ord("q"):
        break
cap.release()
cap.destroyAllWindows
