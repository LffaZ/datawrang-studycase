import requests
query = "ayam"
url = "https://api.x.com/2/tweets/search/recent"

headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAHdGzAEAAAAANuMwm6T61VzGXqoEBIpvzerhmFo%3D0gLDAzoGwmOmI2JJywQ4Krhlagv4STIY9bAoDRujkxpHMLHXAK"}
querystring = {"query":"ayam"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)