import cv2
import numpy as np
import requests
import base64
from matplotlib import pyplot as plt

# url ="http://127.0.0.1:8000/KopiSelection/"
url = "http://iampamungkas.pythonanywhere.com/KopiSelection/"

# imageUrl = "lxv3cm91bk2y.jpg"
imageUrl = "hoho.jpg"

payload = {"image": open(imageUrl, "rb")}


r = requests.post(url, files=payload).json()

img = base64.b64decode(r["image"])
npimg = np.fromstring(img, dtype=np.uint8)
source = cv2.imdecode(npimg, 1)

plt.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB))
plt.show()
