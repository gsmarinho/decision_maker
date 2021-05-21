#!/usr/bin/python

import requests, json, cgi, cgitb, datetime

#Tom's closet :)


item ="""[ {"type":"short", "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBc7hkfdWplcp6NeCEkURgIDlhU0BPpnf7DA&usqp=CAU", "style":"casual", "temp":"hot", "color":"blue" }
, {"shorts2":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbhG-XL8_8Trh40BoRiu9PxDndRWBYDZx1-A&usqp=CAU","style":"casual","temp":"hot", "color":"mixed" },
, {"t-shirts1":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCjdQ1tHXFvO9gfosohEDwQjFmpImaJXHCdQ&usqp=CAU","style":"casual", "temp":"hot", "color":"white" }
, {"t-shirts2":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7jFRS30wG2T6FmXfJtdSj_LfeCHBbB-DrMw&usqp=CAU","style":"casual", "temp":"hot", "color":"blue"  }
, {"pants_casual1":"https://data.tieapart.com/imgprodotto/mens-trousers-with-side-pockets-rope-colored_10799.jpg"}
, {"pants_party1":"https://images.halloweencostumes.com/products/51536/1-1/holographic-disco-pants-for-men.jpg"}
, {"pants_casual2":"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-691910437-1-1551118905.jpg?crop=0.502xw:1.00xh;0.234xw,0&resize=640:*"}
, {"pants_formal11":"https://www.mytailorstore.com/image/cache/catalog/dress%20pants/7317-525x700.jpg"}
, {"shirts1":"https://i.pinimg.com/originals/4c/51/58/4c51580aaeea7c57aedbebfd564ca8c4.jpg"}
, {"shirts2":"https://images-na.ssl-images-amazon.com/images/I/818rZxa6D8L._AC_UY1000_.jpg"}
, {"shirts3":"https://i.pinimg.com/originals/83/cb/fd/83cbfdc0579c0b4def77086d95dc5e97.jpg"}
, {"jacket1":"https://www.dhresource.com/0x0/f2/albu/g10/M01/75/E3/rBVaVly9Os6AGim8AAHYUSnlV0Y613.jpg"}
,{"jacket2":"https://i.pinimg.com/originals/48/5b/fe/485bfe1d051a3b3664f20cb7e40e2f49.jpg"}
, {"jacket3":"https://image.made-in-china.com/43f34j00QyPTHkcMHgqv/Mens-Heavy-Insulated-Parka-Jacket-Winter-Jacket.jpg"}
]"""
closet = json.loads(item)


api_key = "db1b94f0666622aeaf55828924e219a3"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
#city_name= input ("Enter City name: ")
#requests.get('https://api.ipdata.co', verify=False)
#r = requests.get('https://api.ipdata.co?api-key=ac38ee14ba0d81375f9c13a487df6a8f8f4a9ceb424c9490c28fdaeb',verify=False).json()
#city_name = r['country_name']
form = cgi.FieldStorage()
city_name = str(form.getvalue('city'))
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x= response.json()
weekno = datetime.datetime.today().weekday()
print ("Content-type:text/html\r\n\r\n")
if x ["cod"] !="404":
	y = x["main"]
	current_temperature = y["temp"]
	temp = current_temperature # temp in kelvin
	temp = int((temp - 273.15) * 1.8000 + 32) #from Kelvin to Fahrenheit and converting to integer
	if temp > 99:
		if weekno < 5:
			print(item("pants_formal1"))
			print(item("shirts1"))
			
		else:
			print(item[shorts][0])
			print(item[t-shirts][0])
	if temp > 69:
		if weekno < 5:
                        print(item[pants][formal][0])
                        print(item[shirts][0])
		else:
                        print(item[pants][casual][0])
                        print(item[t-shirts][0])
	if temp < 69:
		if weekno < 5:
			print(item[pants][formal][0])
			print(item[shirts][0])                        
			print(item[jacket][0])
		else:
                        print(item[pants][casual][0])
                        print(item[shirts][0])
else:
	print ("City not found")
