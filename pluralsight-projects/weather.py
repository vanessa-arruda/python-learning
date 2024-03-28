import requests

city = "Stockholm"
url = "https://api.weatherapi.com/v1/current.json?key=0f2f9f00099346d4a61151259242703&q="+city+"&aqi=no"

response = requests.get(url)
weather_json = response.json()

temperature = weather_json.get("current").get("temp_f")
description = weather_json.get("current").get("condition").get("text")

print("Today's weather in", city, "is", description, "and", temperature ,"°F")
