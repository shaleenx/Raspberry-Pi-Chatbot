import os
import glob
import random
from time import sleep

class xkcd_api:

	def get_xkcd(self,phone):
		f=open('xkcd/send.txt','w')
		
		phone=phone.split('@')[0]
		print phone
		number=random.randint(1,1050)
		print "Sending Comic number: ", number
		for i in glob.glob('xkcd/img/'+str(number)+'.png'):
			f.write('/L'+"\n"+"/image send "+phone+" "+i)
			print i
		print "File Written"
		f.close()
		sleep(2)
		os.system('./xkcd/send.sh < xkcd/send.txt &')
		sleep(10)
