from urllib import response
import requests

BASE="http://127.0.0.1:5000/"

response = requests.post(BASE + "helloworld/Apoorv Chaudhary/7")

print(response.json())