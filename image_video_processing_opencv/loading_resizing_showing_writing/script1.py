import cv2

image = cv2.imread('galaxy.jpg', 0)

resized_image = cv2.resize(image, (int(image.shape[1] / 3), int(image.shape[0] / 3)))
cv2.imwrite('resized_galaxy.jpg', resized_image)
cv2.imshow("Galaxy", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()