import requests
import pprint
import json
option = input('1. Softcore 2. Hardcore 3. Standard\n')

response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Ancestor&type=Currency')

if option == 1:
    response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Ancestor&type=Currency')
if option == 2:
    response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Ancestorhc&type=Currency')
if option == 3:
    response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Standard&type=Currency')


dict = response.json()

currencies = [{'dict':x,'val':0} for x in dict['lines']]

#dict=[a.b.c]
#currencies =

for x in range(106):
    data = (currencies[x]) #info for every currency
    profitmargin1 = (data['receiveSparkLine']['totalChange'] -data['paySparkLine']['totalChange'])
    profitmargin2 = (data['paySparkLine']['totalChange'] - data['receiveSparkLine']['totalChange'])
    profitmargin3 = max(profitmargin1,profitmargin2)
    profitmarginfinal = round(profitmargin3,8)
    currencies[x]['val']=profitmarginfinal

currencies=sorted(currencies,key=lambda x: -x['val'])

for x in range(109):
    data=(currencies[x]['dict']) 
    print(data['currencyTypeName'], '|', currencies[x]['val'],' chaos profit')

input('Press the Enter key to exit...')