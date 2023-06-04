import cv2
import numpy as np

img_path="PV/133126718323233112.png"
image = cv2.imread(img_path)

grayscale_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Apply a threshold to the image
threshold_img = cv2.threshold(grayscale_img, 127, 255, cv2.THRESH_BINARY)[1]

# Find the contours in the image
contours, hierarchy = cv2.findContours(threshold_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour in the image
largest_contour = max(contours, key=cv2.contourArea)

# Draw a rectangle around the largest contour
cv2.drawContours(image, [largest_contour], 0, (0, 255, 0), 2)

# Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()