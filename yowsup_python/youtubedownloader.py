import mechanize,re
import os
import sys

class song_api:
	
	def download(self,name,format,directory):
		if(os.path.isdir(directory)==True):
		
			br=mechanize.Browser(factory=mechanize.RobustFactory())
			br.set_handle_robots(False)
			
			
			name1=name
			name=name.split(' ')
			temp=''

			for i in name:
				temp=temp+i+'+'
			temp=temp[0:len(temp)-1]
			youtube='https://www.youtube.com/'
			youtube=youtube+'results'+'?'+'search_query'+'='+temp
			from time import sleep
			sleep(2)

			try:
				r=br.open(youtube)
				f=open('y.txt','w')
				a=br.find_link(url_regex=re.compile('watch'),nr=0)
			except:
				return -1

			br1=mechanize.Browser(factory=mechanize.RobustFactory())
			br1.set_handle_robots(False)

			link='http://keepvid.com/?url='+'https://www.youtube.com'+a.url

			try:
				b=br1.open(link)
			
				a=br1.find_link(text_regex=re.compile("Download 3GP"),nr=0)
			except:
				a=br.find_link(url_regex=re.compile('watch'),nr=1)
				b=br1.open(link)
				try:
					a=br1.find_link(text_regex=re.compile("Download 3GP"),nr=0)
				except:
					return -1

			try:
				if(format=='mp4'):
					if(directory!=''):
						f=br1.retrieve(a.url,directory+'/'+name1+'.mp4')[0]
					else:
						f=br1.retrieve(a.url,name1+'.mp4')[0]
				else:
					if(directory!=''):
						f=br1.retrieve(a.url,directory+'/a.3gp')[0]
					else:
						f=br1.retrieve(a.url,'a.3gp')[0]
			except:
				return -2
			return 0
		else:
			return -2

	def send_song(self,phone):
		f=open('./videosongs/send.txt','w')
		f.write('/L\n/audio send '+phone+' ./videosongs/a.3gp')
		os.system('./videosongs/send.sh < ./videosongs/send.txt &')