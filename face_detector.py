import cv2 as cv

img = cv.imread("assets/images/murtaz.jpeg")

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=8,
    minSize=(60, 60)
)
for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h),(0,255,0), 2)
    cv.putText(img, "Face detected", (x, y-30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv.imshow("Face detection", img)
cap = cv.VideoCapture(0)
while True: 
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    facess = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=8,
        minSize=(60, 60)
    )  
    for (x,y,w,h) in facess:
        cv.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)
        cv.putText(frame, "Face detected", (x, y-30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv.imshow("Webcam", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()