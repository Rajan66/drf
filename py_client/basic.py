import requests

# endpoint ="https://httpbin.org/"
# endpoint ="https://httpbin.org/anything"
endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint,json={"query":"Hello world"}) # HTTP request
print(get_response.text) # prints raw text response (HTML)
print(get_response.json())
# print(get_response.json()['message'])
# HTTP Request -> HTML
# REST API HTML Request -> JSON(XML)
# JSON -> Pyth Dict


print(get_response.status_code)