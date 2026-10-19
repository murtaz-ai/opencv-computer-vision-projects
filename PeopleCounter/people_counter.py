import cv2 as cv

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

cap = cv.VideoCapture(0)
while True: 

    ret, frame = cap.read()

    if not ret:
        break

    (boxes, weights) = hog.detectMultiScale(
    frame,
    winStride=(8, 8),
    padding=(4, 4),
    scale=1.05
    )
 
    for (x,y,w,h) in boxes:
        cv.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)
    
    count = len(boxes)
    text = "People Count: " + str(count)

    cv.putText(frame, text, (20, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

    cv.imshow("People counter", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()