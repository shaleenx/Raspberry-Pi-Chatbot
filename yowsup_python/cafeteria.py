class cafeteria_api:

	def shinestar(self):
	    f=open("Shinestar.txt","r")
	    content=f.readlines()
	    return "Shinestar\n"+str(content[0].rstrip())+'\n'+str(content[1].rstrip())+'\n'+str(content[2].rstrip())+'\n'+str(content[3].rstrip())+'\n'+str(content[4].rstrip())+'\n'+str(content[5].rstrip())+'\n'+str(content[6].rstrip())+'\n'+str(content[7].rstrip())+"\n\n"

	def honeyone(self):
	    f=open("Honeyone.txt","r")
	    content=f.readlines()
	    return "Honeyone\n"+str(content[0].rstrip())+'\n'+str(content[1].rstrip())+'\n'+str(content[2].rstrip())+'\n'+str(content[3].rstrip())+'\n'+str(content[4].rstrip())+'\n'+str(content[5].rstrip())+"\n\n"

	def padmakamal(self):
	    f=open("Padmakamal.txt","r")
	    content=f.readlines()
	    return "Padmakamal\n"+str(content[0].rstrip())+'\n'+str(content[1].rstrip())+'\n'+str(content[2].rstrip())+'\n'+str(content[3].rstrip())+'\n'+str(content[4].rstrip())+'\n'+str(content[5].rstrip())+'\n'+str(content[6].rstrip())+'\n'+str(content[7].rstrip())+"\n\n"

	def get_menus(self):
		temp=''
		temp=temp+self.shinestar()
		temp=temp+self.padmakamal()
		temp=temp+self.honeyone()
		return temp