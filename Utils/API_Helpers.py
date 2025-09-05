import requests
from Config.api_config import APIConfig 

class APIClient:
    def __init__(self):
        self.base_url = APIConfig.QA_URL
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {APIConfig.AUTH_TOKEN}"
        }

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers or self.headers, params=params)
        return response

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=headers or self.headers, json=data)
        return response

    def put(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, headers=headers or self.headers, json=data)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers or self.headers)
        return response
