import mechanize
import json
from pprint import pprint
br=mechanize.Browser()
f=open('weather_data.txt','w')
br.set_handle_robots(False)
class weather_api:
	def get_weather(self,city):
	
		br.open('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=63113595ad6bb37132b7d51aebba19cf&units=metric')
		f.write(br.response().read())
		f.close()
		f=open('weather_data.txt','r')

		with open('data.txt') as data_file:    
		    data = json.load(data_file)
		if(data['name'].lower()!=city.lower()):
			print "Enter a valid city name"
			return "Enter a valid city name"
		else:
			print data['name']
			print data['main']['temp']
			print str(data['main']['humidity'])+' '+'%'
			print data['weather'][0]['description']
			print str(data['wind']['speed'])+' '+'mps'
			temp=data['name']+"\n"+data['weather'][0]['description']+"\n"+data['main']['temp']+"\n"+str(data['main']['humidity'])+' '+'%'+"\n"+str(data['wind']['speed'])+' '+'mps'
			return temp
