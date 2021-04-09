import requests, json
api_key = "db1b94f0666622aeaf55828924e219a3"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name= input ("Enter City name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x= response.json()

if x ["cod"] !="404":
    y = x["main"]
    current_temperature = y["temp"] #store the "temp" value key of y
    current_humidity= y["humidity"] #sore humidity value key of y
    z = x["weather"] #store the value of "weather" key in variable z
    temperature = int (current_temperature) #temperature in Kelvin
    temperature = int(temperature * (9 / 5) - 459.67) #from Kevin to fahrenheit and convert to integer
    weather_description = z [0] ["description"]
    print("Temperature: ", temperature, "F",  "\nHumidity: " , current_humidity, "%", "\nDescription: ", weather_description)
else:
    print ("City not found")
