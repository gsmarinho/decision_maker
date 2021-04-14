# Weather check test

import requests, json
api_key = "db1b94f0666622aeaf55828924e219a3"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name= input ("Enter City name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x= response.json()

if x ["cod"] !="404":
    y = x["main"]
    current_temperature = y["temp"]
    temp = int (current_temperature) # temp in kelvin
    temp = temp * (9 / 5) - 459.67 #from Kelvin to Fahrenheit
    print("Temperature: ", temp)
else:
    print ("City not found")
if temp > 69:
   print ("Jeans and light Jacket")
if temp < 69:
   print ("Jeans and heavy Jacket")
