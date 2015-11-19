import os
import glob
import random
from time import sleep

class calvin_api:

	def get_calvin(self,phone):
		f=open('calvin/send.txt','w')
		
		phone=phone.split('@')[0]
		print phone
		number=random.randint(1,68)
		print "Sending Comic number: ", number
		for i in glob.glob('calvin/img/'+str(number)+'.gif'):
			f.write('/L'+"\n"+"/image send "+phone+" "+i)
			print i
		print "File Written"
		f.close()
		sleep(2)
		os.system('./calvin/send.sh < calvin/send.txt &')
		sleep(10)
