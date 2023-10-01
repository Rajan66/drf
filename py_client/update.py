import requests


endpoint = "http://localhost:8000/api/products/6/update/"

data={
    'title':"Hieeeeeeeeeeeee",
    'price':199.99,
}

get_response = requests.put(endpoint,json=data) 
 
print(get_response.json())


