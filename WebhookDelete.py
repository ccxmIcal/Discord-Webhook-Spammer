import json
import requests


with open('config.json', 'r') as f:
    data = json.loads(f.read())
    URL = data['url']


r = requests.delete(URL)
print('Webhook has has been deleted.')