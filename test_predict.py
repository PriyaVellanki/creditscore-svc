import requests

url = "http://127.0.0.1:9696/creditscore"

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
res= requests.post(url, json=client).json()


print(res)