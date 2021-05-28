#!/usr/bin/python

import requests, json, cgi, cgitb, datetime, random

def lookup_closet(closet,clothing_type,clothing_style):
	l = []
	for clothing in closet:
		if clothing["type"] == clothing_type and clothing["style"] == clothing_style:
		#	print("<img src=\"")
		#	print(clothing["image_url"])
		#	print("\">")
		#	return()
			l.append(clothing["image_url"])
	#print(l)
	count = len(l)
	#print(count)
	i = random.randint(0,count - 1 )
	#print(i)
	print("<img src=\"")
	print(l[i])
	print("\">")
	#return(l[i])

#Tom's closet :)

item = """[ {"type":"short", "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBc7hkfdWplcp6NeCEkURgIDlhU0BPpnf7DA&usqp=CAU", "style":"casual", "temp":"hot", "color":"blue" }
, {"type":"short", "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbhG-XL8_8Trh40BoRiu9PxDndRWBYDZx1-A&usqp=CAU","style":"casual","temp":"hot", "color":"mixed" }
, {"type":"t-shirt","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCjdQ1tHXFvO9gfosohEDwQjFmpImaJXHCdQ&usqp=CAU","style":"casual", "temp":"hot", "color":"white" }
, {"type":"t-shirt","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7jFRS30wG2T6FmXfJtdSj_LfeCHBbB-DrMw&usqp=CAU","style":"casual", "temp":"hot", "color":"blue"  }
, {"type":"pants","image_url":"https://data.tieapart.com/imgprodotto/mens-trousers-with-side-pockets-rope-colored_10799.jpg","style":"casual"}
, {"type":"pants","image_url":"https://images.halloweencostumes.com/products/51536/1-1/holographic-disco-pants-for-men.jpg","style":"party"}
, {"type":"pants","image_url":"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-691910437-1-1551118905.jpg?crop=0.502xw:1.00xh;0.234xw,0&resize=640:*","style":"casual"}
, {"type":"pants","image_url":"https://www.mytailorstore.com/image/cache/catalog/dress%20pants/7317-525x700.jpg","style":"formal"}
, {"type":"shirt","image_url":"https://i.pinimg.com/originals/4c/51/58/4c51580aaeea7c57aedbebfd564ca8c4.jpg","style":"formal"}
, {"type":"shirt","image_url":"https://images-na.ssl-images-amazon.com/images/I/818rZxa6D8L._AC_UY1000_.jpg","style":"formal"}
, {"type":"shirt","image_url":"https://i.pinimg.com/originals/83/cb/fd/83cbfdc0579c0b4def77086d95dc5e97.jpg","style":"casual"}
, {"type":"jacket","image_url":"https://www.dhresource.com/0x0/f2/albu/g10/M01/75/E3/rBVaVly9Os6AGim8AAHYUSnlV0Y613.jpg"}
, {"type":"jacket","image_url":"https://i.pinimg.com/originals/48/5b/fe/485bfe1d051a3b3664f20cb7e40e2f49.jpg"}
, {"type":"jacket","image_url":"https://image.made-in-china.com/43f34j00QyPTHkcMHgqv/Mens-Heavy-Insulated-Parka-Jacket-Winter-Jacket.jpg"}
, {"type":"pants","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNVvFkjUWVBSjo76-xZ6O6nQ5yjiF29bVo0A&usqp=CAU","style":"formal"}
, {"type":"pants","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtbZYBhwN9mWWvy81OWi59GkwGvy0BdzCfpg&usqp=CAU","style":"formal"}
, {"type":"shirt","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXrgUNLqS52jSSd3Z_NYHwjm0x4bHd2vlGBw&usqp=CAU","style":"formal"}
, {"type":"shirt","image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1vETto2N_kSCgeQDlsZSRQiwByoHc82DwHg&usqp=CAU","style":"formal"}
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
			lookup_closet(closet,"pants","formal")
			lookup_closet(closet,"shirt","formal")
			
		else:
			lookup_closet(closet,"short")
			lookup_closet(closet,"t-shirt")
	if temp > 69:
		if weekno < 5:
                        lookup_closet(closet,"pants","formal")
                        lookup_closet(closet,"shirt","formal")
		else:
                        lookup_closet(closet,"pants","casual")
                        lookup_closet(closet,"t-shirt","casual")
	if temp < 69:
		if weekno < 5:
			lookup_closet(closet,"pants","formal")
			lookup_closet(closet,"shirt","formal")               
			lookup_closet(closet,"jacket")
		else:
                        lookup_closet(closet,"pants","casual")
                        lookup_closet(closet,"shirt","casual")
else:
	print ("City not found")
