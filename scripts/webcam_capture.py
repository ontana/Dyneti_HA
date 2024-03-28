import uuid

import cv2
import requests
import base64


def capture_image_from_webcam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    ret, frame = cap.read()
    cap.release()

    if ret:
        return frame
    else:
        raise IOError("Failed to capture image from webcam")


def image_to_base64_string(image):
    _, buffer = cv2.imencode('.jpg', image)
    base64_image_str = base64.b64encode(buffer).decode('utf-8')
    return base64_image_str


def send_image_to_api(name, image_base64, single_result=False):
    api_url = 'http://127.0.0.1:5000/classification'
    data = {
        'name': name,
        'image': image_base64,
        'single_result': single_result
    }
    response = requests.post(api_url, json=data)

    return response


image = capture_image_from_webcam()
base64_image_string = image_to_base64_string(image)
response = send_image_to_api(str(uuid.uuid4()), base64_image_string, single_result=False)
print(f"Processed: {response.status_code}, {response.text}")

image_data = base64.b64decode(base64_image_string)

# Write the binary image data to a file
with open('output_image.jpg', 'wb') as file:
    file.write(image_data)