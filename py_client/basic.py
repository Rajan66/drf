import requests

# endpoint ="https://httpbin.org/"
# endpoint ="https://httpbin.org/anything"
# endpoint = "http://localhost:8000/api"
endpoint = "http://localhost:8000/api/demo"

get_response = requests.get(endpoint,json={"product_id":123}) # HTTP request
print(get_response.text) # prints raw text response (HTML)
print(get_response.json())
print(get_response.headers)
# print(get_response.json()['message'])
# HTTP Request -> HTML
# REST API HTML Request -> JSON(XML)
# JSON -> Pyth Dict


print(get_response.status_code)