import glob # glob.glob method takes a path or a pattern and finds all those files' names and makes a list
import cv2

c = 1
for image_name in glob.glob('*.jpg'):
    image = cv2.imread(image_name, 1)
    resized_image = cv2.resize(image, (100, 100))
    resized_image_name = 'resized_image' + str(c) + '.jpg'
    cv2.imwrite(resized_image_name, resized_image)
    c = c + 1
