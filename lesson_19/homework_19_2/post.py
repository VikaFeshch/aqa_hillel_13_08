import requests

url = 'http://127.0.0.1:8080/uploads'
image_path = 'example.jpg'

with open(image_path, 'rb') as img:
    files = {'image': img}
    response = requests.post(url, files=files)

print(response.status_code)
print(response.json())
