# HKO Weather

A simple library to get the hong kong weather information by reading [RSS feeds](http://rss.weather.gov.hk/rsse.html) provided by The Hong Kong Observatory

# Basic Usage

import hko_weather
print(hko_weather.nine_days_forecast().text())
