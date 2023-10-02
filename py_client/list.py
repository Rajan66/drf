import requests
from getpass import getpass

# endpoint = "http://localhost:8000/api/products/"
auth_endpoint = "http://localhost:8000/api/auth/"
password = getpass()

auth_response = requests.get(
    auth_endpoint, json={'username': 'cfe', 'password': password})
# get_response = requests.get(endpoint)

print(auth_response.json())
