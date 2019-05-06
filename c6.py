l2,l3,l4,l5,l=[],[],[],[],[]
t=1
while(t>=1):
	k=0  
	count=0
	row=int(input("enter rows"))
	coloumn=int(input("enter coloumns"))
	l1= [[0 for j in range(coloumn)] for i in range(row)]
	for i in range(row):
		for j in range(coloumn):
			l1[i][j] = input()
	for i in range(row):
		for j in range(coloumn):
			if((i==0 and l1[i][j]!='*')or((j==0 and i>0) and l1[i][j]!='*')or(((i>0 and j>0)and l1[i][j]!='*')and((l1[i-1][j]=='*')or(l1[i][j-1]=='*')))): 
				k=k+1
				l2.append(k) 
				l4.append(i) 
				l5.append(j) 		
	print("across")								
	for i in range(row):
		for j in range(coloumn):
			count=count+1
			if(count==1): 
				d=i       
				e=j       
			if(l1[i][j]== '*'): 
				for a in(a for a in range(len(l4)) if(l4[a]==d and l5[a]==e)):
					print(l2[a],".",end="")
					for p in l:
						print(p,end="")
					print("\n")
				del l[0:len(l)]	
				count=0         
			else:
				l.append(l1[i][j]) 
		if(((i+1)<(row-1)) and(l1[i+1][0]!='*' and l1[i][j]!='*')):         
			for f in(f for f in range(len(l4)) if(l4[f]==d and l5[f]==e)):
				print(l2[f],".",end="")
				for p in l:
					print(p,end="")
				print("\n")
			del l[0:len(l)]
			count=0					
	for a in (a for a in range(len(l4)) if(l4[a]==d and l5[a]==e)):
		print(l2[a],".",end="")
		for p in l:
			print(p,end="")
		print("\n")
	count=0
	del l[0:len(l)]
	print("down")
	for j in range(coloumn):
		for i in range(row):
			count=count+1
			if(count==1):
				d=i																														
				e=j
			if(l1[i][j]== '*'):
				for a in (a for a in range(len(l4))if(l4[a]==d and l5[a]==e)):
					print(l2[a],".",end="")
					for p in l:
						print(p,end="")
					print("\n")	
				del l[0:len(l)]
				count=0
			else:
				l.append(l1[i][j])
		if(((j+1)<=(coloumn-1)) and(l1[0][j+1]!='*' and l1[i][j]!='*')):
			for f in (f for f in range(len(l4))if(l4[f]==d and l5[f]==e)):
				print(l2[f],".",end="")
				for p in l:
					print(p,end="")
				print("\n")	
			del l[0:len(l)]
			count=0	
	for a in (a for a in range(len(l4))if(l4[a]==d and l5[a]==e)):
		print(l2[a],".",end="")
		for p in l:
			print(p,end="")	
		print("\n")
	del l[0:len(l)]
	count=0
	s=input("enter next puzzle first letter:")
	if(s =='O'):
		t=0
	else:
		t=t+1
														
										
