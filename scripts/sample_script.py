import os
import base64
import requests


def encode_image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def send_image_to_api(image_base64):
    # API endpoint
    api_url = 'http://127.0.0.1:5000/classification'
    data = {
        'image': image_base64
    }
    response = requests.post(api_url, json=data)

    return response


image_folder = 'sample'
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

for image_file in image_files:
    full_path = os.path.join(image_folder, image_file)
    image_base64 = encode_image_to_base64(full_path)
    response = send_image_to_api(image_base64)
    print(f"Processed {image_file}: {response.status_code}, {response.text}")
