# -*- coding: utf-8 -*-

import requests
from gi.repository import Notify

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
Notify.init("Price")
Notify.Notification.new(u"Like, right now .. Bitcoins are like £" + r.json()['bpi']['GBP']['rate'] + " each.").show()
