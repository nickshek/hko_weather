import requests
from xml.etree import ElementTree

RSS_FEED_LIST = {

   'nine_days_forecast': "http://rss.weather.gov.hk/rss/SeveralDaysWeatherForecast_uc.xml",
}

def nine_days_forecast():
    r = requests.get(RSS_FEED_LIST["nine_days_forecast"])
    tree = ElementTree.fromstring(r.content)
    item = tree.findall('channel/item')
    feed=[]
    for entry in item:
        #get description, url, and thumbnail
        desc = entry.findtext('description')
        feed.append([desc])
    return feed
