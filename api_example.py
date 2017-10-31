import cv2
import numpy as np
import requests
import base64

# url ="http://127.0.0.1:8000/KopiSelection/"
url = "http://iampamungkas.pythonanywhere.com/KopiSelection/"

imageUrl = "iampamungkas/Downloads/dummy-2.jpg"

payload = {"image": open(imageUrl, "rb")}


r = requests.post(url, files=payload).json()

img = base64.b64decode(r["image"])
npimg = np.fromstring(img, dtype=np.uint8)
source = cv2.imdecode(npimg, 1)

cv2.imshow("Result", source)
cv2.waitKey(0)
