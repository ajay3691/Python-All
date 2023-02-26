import json

import requests

user_Response=requests.get('https://dummyjson.com/users')

print(user_Response)
user = user_Response.json()
print(user)