import os
import glob
import random
from time import sleep

class cyhap_api:

	def get_cyhap(self,phone):
		print "Cyhap"
		f=open('cyhap/send.txt','w')
		
		phone=phone.split('@')[0]
		print phone
		number=random.randint(1,107)
		print "Sending Comic number: ", number
		for i in glob.glob('cyhap/img/'+str(number)+'.png'):
			f.write('/L'+"\n"+"/image send "+phone+" "+i)
			print i
		print "File Written"
		f.close()
		sleep(2)
		os.system('./cyhap/send.sh < ./cyhap/send.txt &')
		sleep(10)
