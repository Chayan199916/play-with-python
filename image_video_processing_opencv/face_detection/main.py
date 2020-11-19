import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('reshav.jpeg')
detected_img = img

gray = cv2.cvtColor(detected_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5)

for x, y, z, w in faces:
    detected_img = cv2.rectangle(detected_img, (x, y), (x + w, y + z), (0, 255, 0), 3)
# print(faces)

# resized = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))


cv2.imshow('Detected Face', detected_img)
cv2.waitKey(0)
cv2.destroyAllWindows()