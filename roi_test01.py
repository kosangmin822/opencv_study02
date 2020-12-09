import cv2

img = cv2.imread('images/2.jpg')
px = img[340, 200]
print(px)

B = img.item(340, 200, 0)
G = img.item(340, 200, 1)
R = img.item(340, 200, 2)

BGR = [B, G, R]
print(BGR)

print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow('original', img)

subimg = img[300:400, 350:750]
cv2.imshow('cutting', subimg)

img[300:400, 0:400] = subimg

print(img.shape)
print(subimg.shape)

cv2.imshow('modified', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

b, g, r = cv2.split(img)

print(img[100, 100])
print(b[100, 100], g[100, 100], r[100, 100])

cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)

cv2.waitKey(0)
cv2.destroyAllWindows()

merged_img = cv2.merge((b, g, r))
cv2.imshow('merged', merged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
