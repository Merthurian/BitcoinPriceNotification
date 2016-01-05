import requests

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(r.json()['bpi']['GBP']['rate'])
