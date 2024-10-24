import requests

filename = 'example.jpg'
response = requests.get(f'http://127.0.0.1:8080/uploads/{filename}')

if response.status_code == 200:
    with open('received_image.jpg', 'wb') as f:
        f.write(response.content)
    print('Image received successfully.')
    print('Image saved as received_image.jpg.')
else:
    print('Failed to get image. Status code:', response.status_code)
    print('Response:', response.text)
