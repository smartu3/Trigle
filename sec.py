# -*- coding: UTF-8 -*-



def tri(x):
	dict={}
	tris=[]
	for i in range(1,x+1):
		for j in range(1,i+1):
			if j == 1:
				a = "%d,%d" % (i,j)
				dict[a] = 1 
			if j == i :
				a = "%d,%d" % (i,j)
				dict[a] = 1 
				break
			if j >1 and j < i :
				a,b,c = "%d,%d" % (i,j),"%d,%d" % (i-1,j),"%d,%d" % (i-1,j-1)
				dict[a] = dict[b] +dict[c]
	for i in range(1,x+1):
		strf=''
		for j in range(1,i+1):
			a="%d,%d" % (i,j)
			if j == i:
				strf += str(dict[a])
				break
			strf += str(dict[a])+' '
		print strf.center(50)

