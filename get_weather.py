import requests

x = requests.get('https://api.agify.io/?name=ilan')
print(x.json().get("age"))
