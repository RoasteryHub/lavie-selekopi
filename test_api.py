import cv2
import numpy as np
import requests
import base64

url ="http://127.0.0.1:8000/KopiSelection/"

#img = cv2.imread('/Users/iampamungkas/Downloads/cherries.jpg',0)

image = cv2.imread("/Users/iampamungkas/Downloads/cherries.jpg")
payload = {"image": open("/Users/iampamungkas/Downloads/cherries.jpg", "rb")}

#payload = {"path": "/Users/iampamungkas/Downloads/cherries.jpg"}

r = requests.post(url, files=payload).json()

#print "/Users/iampamungkas/Downloads/cherries.jpg: {}".format(r)

img = base64.b64decode(r["image"])
npimg = np.frombuffer(img, dtype="uint8");
source = cv2.imdecode(npimg, 0)

cv2.imshow("Nyoba",npimg)
cv2.waitKey(0)