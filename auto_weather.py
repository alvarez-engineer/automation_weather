import requests
from bs4 import BeautifulSoup

# Break the lat and long per user and save that in a database
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]


current_conditions = soup.find(id="current-conditions")
location = [l.get_text() for l in current_conditions.select(".panel-title")]
location = location[0]
#string split at (
print(current_conditions.prettify())
#print(location)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

import pandas as pd
weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temp": temps,
        "desc":descs
    })
## weather

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')

## weather["temp_num"].mean()

##is_night = weather["temp"].str.contains("Low")
##weather["is_night"] = is_night

## weather[is_night]

##Compare yesterday's temp to todays and tell me if its going to be colder or warmer
##Can also compare it to Waxhaw and Florida

temp_today_high = weather.iloc[0,4]
temp_today_low = weather.iloc[1,4]

## Automated text include
## Today's high and low temp
## This weeks high and low temp
##  Sunny or Cloudy
week_high_period = weather["period"].loc[weather["temp_num"].idxmax()]
week_high_temp = weather["temp"].loc[weather["temp_num"].idxmax()]

week_low_period = weather["period"].loc[weather["temp_num"].idxmin()]
week_low_temp = weather["temp"].loc[weather["temp_num"].idxmin()]

text_strings = "Good morning! \nToday's low will be %s"  % temp_today_low

temp_yester_high = temp_today_high
temp_yester_low = temp_today_low

# print('Today has a high of: ', temp_today_high)
# print('Today has a low of: ',temp_today_low)
#
# print('Week has a high of: ', week_high_temp)
# print('This is on ',week_high_period)
#
# print('Week has a low of: ', week_low_temp)
# print('This is on ',week_low_period)
