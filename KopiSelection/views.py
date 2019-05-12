# Adrian Rosebrock CV boilerplate
# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import cv2
import base64


@csrf_exempt
def detection(request):
    # initialize the data dictionary to be returned by the request
    data = {"success": False}

    # check to see if this is a post request
    if request.method == "POST":
        # check to see if an image was uploaded
        if request.FILES.get("image", None) is not None:
            # grab the uploaded image
            image = _grab_image(stream=request.FILES["image"])

        # otherwise, assume that a URL was passed in
        else:
            # grab the URL from the request
            url = request.POST.get("url", None)

            # if the URL is None, then return an error
            if url is None:
                data["error"] = "No URL provided."
                return JsonResponse(data)

            # load the image and convert
            image = _grab_image(url=url)

        # START WRAPPING OF COMPUTER VISION APP

        # v1 = useless
        # Insert code here to process the image and update
        # img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Otsu's thresholding after Gaussian filtering
        # blur = cv2.GaussianBlur(img_grey, (5, 5), 0)
        # blur = cv2.bilateralFilter(img_grey, 5,200,200)
        # retval,th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)

        # v1 ends here

        # v2 start here

        # Let's try something here
        red_upper = np.array([207, 128, 255], np.uint8)
        red_lower = np.array([0, 00, 159], np.uint8)
        green_upper = np.array([0, 00, 159], np.uint8)
        green_lower = np.array([0, 00, 70], np.uint8)
        # convert to HSV if we wan tto use video as input
        # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Construct mask for the ripe one
        mask = cv2.inRange(image, red_lower, red_upper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)


        green_mask = cv2.inRange(image, green_lower, green_upper)
        green_mask = cv2.erode(green_mask, None, iterations=2)
        green_mask = cv2.dilate(green_mask, None, iterations=2)
        # Final Step

        # Countour drawing
        im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            # compute the center
            # M = cv2.moments(c)
            # cX = int(M["m10"]/M["m00"])
            # cY = int(M["m01"] / M["m00"])

            # draw the contour and center of the shape on the image
            # cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            # cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
            (x, y), radius = cv2.minEnclosingCircle(c)
            center = (int(x), int(y))
            radius = int(radius)
            if (radius > 15) and (radius <= 80):
                cv2.circle(image, center, 1, (0, 255, 0), 2)
                cv2.putText(image, "Ripe", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


        im2, contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            # compute the center
            # M = cv2.moments(c)
            # cX = int(M["m10"]/M["m00"])
            # cY = int(M["m01"] / M["m00"])

            # draw the contour and center of the shape on the image
            # cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            # cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
            (x, y), radius = cv2.minEnclosingCircle(c)
            center = (int(x), int(y))
            radius = int(radius)
            if (radius > 15) and (radius <= 80):
                cv2.circle(image, center, 1, (0, 255, 0), 2)
                cv2.putText(image, "Not Ripe", (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


        # the `data` dictionary with your results
        retval, buffer = cv2.imencode('.jpg', image)
        data["image"] = base64.b64encode(buffer)
        # END WRAPPING OF COMPUTER VISION APP

        # update the data dictionary
        data["success"] = True

    # return a JSON response
    # data = json.dumps(data)
    return JsonResponse(data)


def _grab_image(path=None, stream=None, url=None):
    # if the path is not None, then load the image from disk
    if path is not None:
        image = cv2.imread(path, 0)

    # otherwise, the image does not reside on disk
    else:
        # if the URL is not None, then download the image
        if url is not None:
            resp = urllib.urlopen(url)
            data = resp.read()

        # if the stream is not None, then the image has been uploaded
        elif stream is not None:
            data = stream.read()
        # convert the image to a NumPy array and then read it into
        # OpenCV format
        image = np.asarray(bytearray(data), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image
