import os

os.system('ls img | sort -g -r > temp')
f = open('temp', 'r')
count = 1;
for i in f.readlines():
	print i[:-1]
	os.system('mv img/'+i[:-1]+' img/'+str(count)+'.png')
	count = count + 1

