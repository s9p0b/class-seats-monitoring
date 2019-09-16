import requests

response = requests.get('https://ubc-courses-api.herokuapp.com/2018W/CPSC/310/L1F')

print(response.json())
