import re
import pprint
import mechanize
import json
class cricket_api:
  f=open('cricket_data.txt','w')
  br=mechanize.Browser()
  br.set_handle_robots(False)
  def get_all_score(self):
    self.f=open('cricket_data.txt','w')
    self.br.open('http://cricscore-api.appspot.com/csa')
    self.f.write(self.br.response().read())
    self.f.close()
    
    temp=''
    with open('cricket_data.txt') as data_file:    
        data = json.load(data_file)
    for i in xrange(0,len(data)):
      temp=temp+str(i)+'. '+data[i]['t1']+"  vs  "+data[i]['t2']+"\n"
    return temp
  def get_single_score(self,i):
    with open('cricket_data.txt') as data_file:    
        data = json.load(data_file)
    url='http://cricscore-api.appspot.com/csa?id='+str(data[i]['id'])
    print url
    self.br.open(url)
    self.f=open('cricket_data.txt','w')
    #self.br.open('http://cricscore-api.appspot.com/csa')
    self.f.write(self.br.response().read())
    self.f.close()
    temp=''
    with open('cricket_data.txt') as data_file:    
        data = json.load(data_file)
    temp=temp+data[0]['si']+"\n"+data[0]['de']
    return temp

