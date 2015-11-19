import mechanize
import json
from pprint import pprint
import re

br=mechanize.Browser()
f=open('weather_data.txt','w')
br.set_handle_robots(False)

class weather_api:
	br=mechanize.Browser()
	f=open('weather_data.txt','w')
	br.set_handle_robots(False)

	def get_weather(self,city):
		city1=city
		city=re.sub(' ','%20',city)
		self.f=open('weather_data.txt','w')
		self.br.open('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=63113595ad6bb37132b7d51aebba19cf&units=metric')
		self.f.write(self.br.response().read())
		self.f.close()
		f=open('weather_data.txt','r')

		with open('weather_data.txt') as data_file:    
		    data = json.load(data_file)

		if(data['name'].lower()!=city1.lower()):
			print "Burrrp! I am afraid I am not aware of this city.\nTry some more popular location nearby."
		else:
			print data['name']
			print str(data['main']['temp'])+' Degree Celsius'
			print str(data['main']['humidity'])+' '+'%'
			print data['weather'][0]['description']
			print str(data['wind']['speed'])+' '+'mps'
			temp=data['name']+"\n"+str(data['weather'][0]['description']).title()+"\n"+str(data['main']['temp'])+" Degree Celsius\n"+str(data['main']['humidity'])+' '+'%'+"\n"+str(data['wind']['speed'])+' '+'mps'
			return temp
