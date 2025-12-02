import requests
import pandas as pd
from datetime import datetime, timedelta

URL = "https://pasig-marikina-tullahanffws.pagasa.dost.gov.ph/water/detail_list.do"

# parameters you must set
station_code = "11105201"
end_time = datetime(2025, 12, 2, 8, 50)
start_time = datetime(2025, 11, 25, 0, 0)

all_rows = []

current = end_time
while current >= start_time:
    timestamp = current.strftime("%Y%m%d%H%M")  # API format

    payload = {
        "obscd": station_code,
        "ymdhm": timestamp
    }

    response = requests.post(URL, data=payload)
    data = response.json()

    # Append if the API returned any data
    if isinstance(data, list) and len(data) > 0:
        all_rows.extend(data)

    # Move to previous measurement (60 mins)
    current -= timedelta(minutes=60)

df = pd.DataFrame(all_rows)

print(df.head())
df.to_csv("historical_water_levels.csv", index=False)