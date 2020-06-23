import cv2
import requests
import time
import base64

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        #img_name = "opencv_frame_{}.png".format(img_counter)
        #cv2.imwrite(img_name, frame)
        img_str = cv2.imencode('.jpg', frame)[1].tostring()
        print("time picture taken:", time.time())
        #print(frame)
        r = requests.post('http://localhost:5000', data=img_str)
        print(r.text)
        #print("{} written!".format(img_name))
        img_counter += 1
        break
    #print(frame)
cam.release()

cv2.destroyAllWindows()