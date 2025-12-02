import requests as req
from datetime import datetime, timedelta
import pandas as pd
import time

url = 'https://pasig-marikina-tullahanffws.pagasa.dost.gov.ph/water/detail_list.do'

start_time = datetime(2025, 11, 25, 0, 0)
end_time = datetime(2025, 12, 2, 8, 50)

all_rows = []

obscd = 11104201
ymdhm = 20251202910

current = end_time

while current >= start_time: 
    timestamp = current.strftime("%Y%m%d%H%M")

    payload = {
        "obscd": obscd,
        "ymdhm": timestamp
    }
    
    resp = req.post(url, data=payload)
    data = resp.json()
    
    if isinstance(data, list) and len(data) > 0:
        all_rows.extend(data)

    current -= timedelta(minutes=60)
    
    time.sleep(60)

df = pd.DataFrame(all_rows)
df.to_csv("historical_water_levels.csv", index=False)