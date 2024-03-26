import requests
import tkinter as tk
import pprint
import json


def currencyquery(option,widget):
    response = None

    if option == 'Softcore':
        response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Ancestor&type=Currency')
    if option == 'Hardcore':
        response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Ancestorhc&type=Currency')

    dict = response.json()

    currencies = dict['lines']

    data = [0] * len(currencies)
    for x in range(len(currencies)):
        data[x] = (currencies[x])

    data.sort

    result = [0] * len(currencies)
    
    for x in range(len(data)):
        #print(data[x]['currencyTypeName'], data[x]['chaosEquivalent'], 'chaos orbs')
        chaos = str(data[x]['chaosEquivalent'])
        widget.insert(tk.END, data[x]['currencyTypeName'] + '\n', '\n',str(data[x]['chaosEquivalent']),chaos, ' chaos orbs\n\n')