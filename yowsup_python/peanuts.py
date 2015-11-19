import os
import glob
import random
from time import sleep

class peanuts_api:

	def get_peanuts(self,phone):
		f=open('peanuts/send.txt','w')
		phone=phone.split('@')[0]
		print phone
		number=random.randint(19,40)
		print "Sending Comic number: ", number
		for i in glob.glob('peanuts/img/'+str(number)+'.jpg'):
			f.write('/L'+"\n"+"/image send "+phone+" "+i)
			print i
		print "File Written"
		f.close()
		sleep(2)
		os.system('./peanuts/send.sh < ./peanuts/send.txt &')
		sleep(10)
