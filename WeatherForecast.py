# -*- coding: utf-8 -*-
__author__ = "1041748 劉耿宇"

import requests
import json


def weather():
  url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Taipei%2C%20Taiwan%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
  w_raw_data = requests.get(url)
  w_raw_data.json()
  w_json_obj = json.loads(w_raw_data.text)


  daliy_weather=[] #用來存取'最高溫' '最低溫''天氣狀況''日期'
  forecast_w = w_json_obj["query"]["results"]["channel"]["item"]["forecast"]

  for i in range(0, 7):
    forecast_high_temperature_F = forecast_w[i]["high"]
    forecast_low_temperature_F = forecast_w[i]["low"]
    forecast_description = forecast_w[i]["text"]
    forecast_Date = forecast_w[i]["date"]
    forecast_high_temperature_C = (float(forecast_high_temperature_F)-32)*5/9
    forecast_low_temperature_C = (float(forecast_low_temperature_F)-32)*5/9
    
    day = []
    day.append(forecast_Date)
    day.append(int(forecast_high_temperature_C))
    day.append(int(forecast_low_temperature_C))
    day.append(str(forecast_description))
    
    daliy_weather.append(day)
  # print(daliy_weather)
  return daliy_weather
