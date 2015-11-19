import mechanize
import json
import re
from pprint import pprint

class news_api:
	br=mechanize.Browser()
	br.set_handle_robots(False)
	f=open('news_data.txt','w')

	def get_news(self,keyword):
		keys=['590a3bf8b43e3373fca8608afc712a4c5d58ecee', '3513017deb8fcf8d9890518e4cb5058553f1753f', 'cf5e5cf38082ea140f2fc334f6265dc1c6a8a410', '620ab8db3145385e533d4dc7f8d4992be894a9d3']
		
		keyword=re.sub(' ','%20',keyword)
		print keyword

		for i in xrange(0,4):
			self.f=open('news_data.txt','w')
			url='https://gateway-a.watsonplatform.net/calls/data/GetNews?outputMode=json&start=now-7d&end=now&count=1&q.enriched.url.enrichedTitle.keywords.keyword.text='+keyword+'&return=enriched.url.url,enriched.url.title,enriched.url.text&apikey='+keys[i]
			self.br.open(url)
			print url
			self.f.write(self.br.response().read())
			self.f.close()
			

			with open('news_data.txt') as data_file:    
			    data = json.load(data_file)
			pprint(data)
			
			if(data['status']!='ERROR'):
				try:
					temp="TITLE: "+data["result"]['docs'][0]['source']['enriched']['url']['title']+"\n"
					temp=temp+data["result"]['docs'][0]['source']['enriched']['url']['text']+"\n"
					temp=temp+ data["result"]['docs'][0]['source']['enriched']['url']['url']
					print temp
					return temp
			
				except Exception as e:
					pass

		return "Burp! No such Trending news"