import requests
import pandas as pd
from bs4 import BeautifulSoup

# This is should be based on the user
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
# For seven day section
seven_day = soup.find(id="seven-day-forecast")
# This is contains all the items for the forecast
forecast_items = seven_day.find_all(class_="tombstone-container")

# For current conditions section
current_conditions = soup.find(id="current-conditions")

# Pulls specifically from that class, "this includes the .class stuff"
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

location_tags = current_conditions.select(".panel-heading .panel-title")
location = [lt.get_text() for lt in location_tags]

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
