import requests

endpoint = "http://127.0.0.1:8000/api/"

reponse = requests.post(endpoint,json={'name':'hrishikesh',"price":'123a'})

print(reponse.json())