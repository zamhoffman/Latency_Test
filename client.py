import requests
import time


print(time.time())
r = requests.post('http://localhost:5000', json={'frame': 1})
print(r.text)