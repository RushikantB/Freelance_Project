import requests
from Config.api_config import APIConfig

'''
class APIClient:
    def __init__(self, use_auth=True):
        self.base_url = APIConfig.QA_URL.rstrip("/")
        self.headers = {"Content-Type": "application/json"}

        # Only add Authorization if token exists and use_auth=True
        if use_auth and getattr(APIConfig, "AUTH_TOKEN", None):
            token = APIConfig.AUTH_TOKEN
            if token:
                self.headers["Authorization"] = f"Bearer {token}"

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=headers or self.headers, params=params)

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = self.headers.copy()
        if headers:
            final_headers.update(headers)
        return requests.post(url, headers=headers or self.headers, json=data)

    def put(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.put(url, headers=headers or self.headers, json=data)

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.delete(url, headers=headers or self.headers)
'''


class APIClient:
    def __init__(self, use_auth=True):
        self.base_url = APIConfig.QA_URL.rstrip("/")
        self.headers = {"Content-Type": "application/json"}

        # Add Authorization if token exists and use_auth=True
        if use_auth and getattr(APIConfig, "AUTH_TOKEN", None):
            token = APIConfig.AUTH_TOKEN
            if token:
                self.headers["Authorization"] = f"Bearer {token}"

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=headers or self.headers, params=params)

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = self.headers.copy()
        if headers:
            final_headers.update(headers)
        return requests.post(url, headers=final_headers, json=data)

    def put(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = self.headers.copy()
        if headers:
            final_headers.update(headers)
        return requests.put(url, headers=final_headers, json=data)

    def patch(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = self.headers.copy()
        if headers:
            final_headers.update(headers)
        return requests.patch(url, headers=final_headers, json=data)

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        final_headers = self.headers.copy()
        if headers:
            final_headers.update(headers)
        return requests.delete(url, headers=final_headers)
