import cv2,skimage
vid = cv2.VideoCapture(0)
while True:
    flag,img = vid.read()
    if flag:
         gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
         blue_img = cv2.subtract(img[:,:-3])
