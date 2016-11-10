#!/usr/bin/env python

# OpenAssistant 0.04
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp

# weather.py - Get Weather Forecast From Dark Sky (darksky.net)

# Get Your API Key And Longitude / Latitude At: https://darksky.net/dev/
# Install 'forecastio' module with: pip install python-forcastio

import forecastio

# Weather For Darmstadt, Germany

api_key = "e3f8667cb539171dc2f4b389d33648ce"
lat = 49.8705556
lng = 8.6494444

forecast = forecastio.load_forecast(api_key, lat, lng)
byHour = forecast.currently()
currentTemp = int(byHour.temperature)

print("The weather is currently {0} ...".format(byHour.summary))

print("The temperature is {0} degrees Celsius ...".format(currentTemp))

byHour = forecast.hourly()
print(byHour.summary)

byHour = forecast.daily()
print(byHour.summary)