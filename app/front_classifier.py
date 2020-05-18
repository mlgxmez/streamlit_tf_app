import streamlit as st
import requests
import json
import base64
import os
import urllib.request
from PIL import Image

def predict(img_file):
    with open(img_file, mode='rb') as file:
        img = file.read()
    data = {"inputs":[{"b64":base64.encodebytes(img).decode("utf-8")}]}
    result = requests.post("http://classifier:8501/v1/models/mobilenet_v2_test:predict", data=json.dumps(data))
    return result.content

image_filename = "downloaded_image.jpeg"   
image_url = st.text_input("Add URL of image:")

if st.button("Classify"):
    image_file, _ = urllib.request.urlretrieve(image_url,image_filename)
    image_class = predict(image_file)
    image = Image.open(image_file)
    st.image(image, "Image selected", width=480)
    st.write(image_class.decode())