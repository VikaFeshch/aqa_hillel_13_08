import requests
import os

class ApiNasaPhoto():

    DEMO_KEY = 'LVKtvhfQ6GtrOFan3fkefHHc8IPWiaAdOUlf2M9W'

    BASE_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

    params = {
        'sol': 1000,
        'camera': 'fhaz',
        'api_key': DEMO_KEY
    }


    def get_request(self):
        response = requests.get(self.BASE_URL, params=self.params)
        return response

    def load_photo(self):
        response = self.get_request()
        if response.status_code == 200:
            data = response.json()
            print(data)
            photos = data.get('photos', [])
            if not photos:
                print("Photos not found")
            else:
                os.makedirs('mars_photos', exist_ok=True)

                for i, photo in enumerate(photos):
                    photo_url = photo['img_src']
                    img_response = requests.get(photo_url)

                    if img_response.status_code == 200:

                        file_path = f'mars_photos/mars_photo{i + 1}.jpg'
                        with open(file_path, 'wb') as file:
                            file.write(img_response.content)
                        print(f'Saved: {file_path}')
                    else:
                        print(f'Failed to upload photo: {photo_url}')
        else:
            print(f'Error request to API: {response.status_code}')

# def request_to_api():
#     api_nasa = ApiNasaPhoto()
#     api_nasa.load_photo()
#     response = api_nasa.get_request()
#     return response
#
# def test_api_nasa_photo():
#     response = request_to_api()
#     assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
#
# def test_exist_photo():
#     response = request_to_api()
#     data = response.json()
#     photos = data.get('photos', [])
#     assert len(photos) > 0, "No photos found in response"


# if __name__ == "__main__":
#     test_api_nasa_photo()
#     print("Тест пройшов успішно!")
api_nasa = ApiNasaPhoto()
api_nasa.load_photo()




