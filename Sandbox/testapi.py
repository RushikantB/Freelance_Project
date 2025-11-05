import requests

'''
r = requests.get("https://reqres.in/api/users?page=1")
print("Status Code: ", r.status_code, r.json())
# print("Final URL: ", r.url())
print("Request headers: ", r.request.headers)
print("Response: ", r.text)
'''

url = "https://reqres.in/api/login"  # login endpoint

payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
