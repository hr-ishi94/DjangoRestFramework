import requests

endpoint = "http://127.0.0.1:8000/api"

reponse = requests.get(endpoint,json={'name':'hrishikesh'},params={'abc':123})

# print(reponse.json())
print(reponse.text)