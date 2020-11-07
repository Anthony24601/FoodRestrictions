from django.shortcuts import render
from django.http import HttpResponse
import cv2
import pytesseract
import numpy as np
import base64


def index(request):
    return render(request, "FRApp/index.html", {})


def scan(request):
    def data_uri_to_cv2_img(uri):
        encoded_data = uri.split(",")[1]
        nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img

    data_uri = request.POST.get("data-uri", "")
    img = data_uri_to_cv2_img(data_uri)
    # cv2.imwrite("test-photo.png", img)
    # print(request.POST.get("image", ""))
    text = pytesseract.image_to_string(img)

    return HttpResponse(text)


# Create your views here.
