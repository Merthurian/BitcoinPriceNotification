# -*- coding: utf-8 -*-

import requests
from gi.repository import Notify

r = requests.get('https://blockchain.info/ticker')
Notify.init("Price")

last = float(r.json()['GBP']['last'])
buy = float(r.json()['GBP']['buy'])
sell = float(r.json()['GBP']['sell'])

Notify.Notification.new(u"last: £" +
    str(last) +
    u" buy: £" +
    str(buy) +
    u" sell: £" +
    str(sell)
    ).show()
