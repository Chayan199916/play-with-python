import glob
import cv2

list_of_image_names = glob.glob("*.jpg")

c = 1
for image_name in list_of_image_names:
    img = cv2.imread(image_name, 1)
    resized_image = cv2.resize(img, (200, 200))
    cv2.imwrite("resized_image" + str(c) + ".jpg", resized_image)
    c = c + 1