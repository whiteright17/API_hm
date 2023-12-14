# my_api_module.py

import requests


class MyApi:
    def __init__(self, url, headers=None, payload=None):
        self.url = url
        self.headers = headers or {}
        self.payload = payload or {}

    def download_image(self, image_type):
        try:
            url = f"{self.url}/image/{image_type}"
            response = requests.get(url, headers=self.headers, data=self.payload)
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Error {image_type}: {e}")
            return None
