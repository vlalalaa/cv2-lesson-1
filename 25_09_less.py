import cv2
image = cv2.imread('image.jpg')
size1  = cv2.resize(image, (700, 400))
cv2.imshow('image', size1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
size  = cv2.resize(gray, (700, 400))
cv2.imshow('gray', size)
border = cv2.Canny(size, 100, 200)
cv2.imshow('border', border)
rotate = cv2.rotate(size1, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotate', rotate)

blur = cv2.GaussianBlur(size, (7, 7), 0)
cv2.imshow('blur', blur)


cv2.waitKey(0)
cv2.destroyAllWindows()
