import requests
import pprint
import json

option = input('1. Softcore 2. Hardcore 3. Standard')

response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Ancestor&type=Currency')

if option == 1:
    response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Ancestor&type=Currency')
if option == 2:
    response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Ancestorhc&type=Currency')
if option == 3:
    response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Standard&type=Currency')

dict = response.json()

currencies = dict['lines']

data = [0] * len(currencies)
for x in range(len(currencies)):
    data[x] = (currencies[x]) #info for every currency
    #print(data['currencyTypeName'],data['pay'])

data.sort

for x in range(len(data)):
    print(data[x]['currencyTypeName'], data[x]['chaosEquivalent'], 'chaos orbs')


input('Press the Enter key to exit...')
