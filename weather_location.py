#weather check test
#added api to get location from web

import requests, json
api_key = "db1b94f0666622aeaf55828924e219a3"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
#city_name= input ("Enter City name: ")
r = requests.get('https://api.ipdata.co?api-key=ac38ee14ba0d81375f9c13a487df6a8f8f4a9ceb424c9490c28fdaeb').json()
city_name = (r['city'])
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x= response.json()
if x ["cod"] !="404":
    y = x["main"]
    current_temperature = y["temp"]
    temp = current_temperature # temp in kelvin
    temp = int(temp * (9 / 5) - 459.67) #from Kelvin to Fahrenheit and converting to integer
    print(city_name)
    print("Temperature: ", temp)
else:
    print ("City not found")
if temp > 69:
    print ("Jeans and light Jacket")
if temp < 69:
    print ("Jeans and heavy Jacket")
