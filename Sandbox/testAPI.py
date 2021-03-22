import requests

#x = requests.get('https://tuuyen.herokuapp.com/api/refrigerators')

x = requests.get('https://tuuyen.herokuapp.com/api/customers/f13e0830-f166-4833-9b41-be215e01a40e', headers={'Authorization': 'Token bae7b78b6c71518e6e2c46949d22a336ca70133f'})

print(x.text)