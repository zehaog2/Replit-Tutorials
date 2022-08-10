import os
import requests
my_secret = os.environ['api'] # go to the website below and use your own API key
API_KEY = my_secret
WS_URL = "http://api.weatherstack.com/current"
cities = []
with open("cities.txt") as f:
	for line in f:
		cities.append(line.strip())
print(cities)

for city in cities:
	parameters = {'access_key': API_KEY, 'query': city}
	response = requests.get(WS_URL, parameters)
	js = response.json()
	ws = js['current']['wind_speed']
	hu = js['current']['humidity'] 
	pr = js['current']['precip']
	t = js['current']['feelslike']
	if(hu > 35 and hu < 65 and ws < 20 and pr < 5):
		print("Good tennis weather in", city, ".\n")
	# humidity->less dense air -> less ball drag -> faster balls
	# humidity 40 -60 is perfect
	# precipitation < 5mm is very light rainfall
	with open(f"{city}.txt", "w") as f:
		f.write(f"Wind speed {ws}\nHumidity {hu}\nRainy {pr}\nFeels like {t} degree\n")
