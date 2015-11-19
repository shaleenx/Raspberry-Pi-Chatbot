import mechanize
import json
import re
from pprint import pprint
br=mechanize.Browser()
br.set_handle_robots(False)
f=open('data.txt','w')
keyword=raw_input("Enter the Keyword")
keyword=re.sub(' ','%20',keyword)
br.open('https://gateway-a.watsonplatform.net/calls/data/GetNews?outputMode=json&start=now-7d&end=now&count=10&q.enriched.url.enrichedTitle.keywords.keyword.text='+keyword+'&return=enriched.url.url,enriched.url.title,enriched.url.text&apikey=3513017deb8fcf8d9890518e4cb5058553f1753f')
f.write(br.response().read())
f.close()
f=open('data.txt','r')

with open('data.txt') as data_file:    
    data = json.load(data_file)

temp="TITLE: "+data["result"]['docs'][0]['source']['enriched']['url']['title']+"\n"
temp=temp+data["result"]['docs'][0]['source']['enriched']['url']['text']+"\n"
temp=temp+ data["result"]['docs'][0]['source']['enriched']['url']['url']
print temp
