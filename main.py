import cv2






image = cv2.imread('image.jpg')


#resizer_code
new_width = int(input("enter desired width"))
new_height = int(input("enter desired height"))
down_points = (new_width, new_height)
resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)

#display original and resized image
cv2.imshow('Original Image', image)
cv2.imshow('resized down', resized_down)
cv2.waitKey()

#close both windows(press any key)
cv2.destroyAllWindows()