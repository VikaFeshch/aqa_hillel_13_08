import requests

filename = 'example.jpg'
delete_url = f'http://127.0.0.1:8080/delete/{filename}'

response = requests.delete(delete_url)

print('Status code:', response.status_code)
print('Response:', response.text)
