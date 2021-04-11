import requests
import os

import json



url = "https://tuuyen.herokuapp.com/api/customers/check_face/"


files=[
  ('file',('au.jpg',open('C:/Users/ASUS/Desktop/au.jpg','rb'),'image/jpeg'))
]

response = requests.request("POST", url, files=files)

print(response)

#text = '{"customerID":"0bdb5ae5-38f3-43b6-85c6-a6c113cfb9a8","username":"popeye","first_name":"Sirawit","last_name":"Sukwattanavit","credit":0}'
# 8 4 4 4 12

# def detection(text):
#   user = json.loads(text)
#   print(user)
#   print(user["customerID"])
#   customerID = user["customerID"].split('-')
#   check_format = [8,4,4,4,12]
#   for i, hex_text in enumerate(customerID):
#     if not len(hex_text) == check_format[i]:
#       return False
  
#   return True

# print(detection(text))
