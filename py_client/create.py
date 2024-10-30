import requests 

endpoint = 'http://localhost:8000/api/product/'

data = {'name' :"Lorry", "price":"250"}
response = requests.post(endpoint, json= data)

print(response.json())