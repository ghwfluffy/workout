#!/usr/bin/env python3

import yaml

#from datetime import date, datetime

from utils.data import get_data
#from utils.datemanip import today, DateDelta, period_to_month_multiplier

data = get_data()

data['exercises'].sort(key=lambda x:x['lastComplete'])
i = 0
for item in data['exercises']:
    if not item['category'] in ["Upper", "Full Body"]:
        continue
    print(item)
    i += 1
    if i > 10:
        break
