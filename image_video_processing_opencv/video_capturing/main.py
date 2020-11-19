import cv2, time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
counter = 1
while True:
    counter = counter + 1
    check, frame = video.read()

    print(check)
    print(frame)
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("image.png", frame)
    cv2.imshow("Captured Image", gray_image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(counter)
video.release()
cv2.destroyAllWindows()