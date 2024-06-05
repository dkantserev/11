m=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ,16]


def rec(m,len,start):
	l=len
	k=start
	
	if l==0:
		print('конец')
	else:
			print(m[k])
			l-=1
			k+=1
			rec(m,l,k)
	
rec(m,len(m),0)
