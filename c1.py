l1,l2=[],[]
m=int(input("enter row"))
c=0
c1=0
b=1
while(b>=1):
	for i in range(0,m*m):
		l1.append(input())
	s=input("enter")
	for d in range(len(l1)):
		if(l1[d]=="_"):
			x=d	
	for k in range(len(s)):
		if(s[k]=='A'and x>=m):
			l1[x],l1[x-m]=l1[x-m],l1[x]
			c=c+1
		if(s[k]=='B'and x<=(len(l1)-(m+1))):
			l1[x],l1[x+m]=l1[x+m],l1[x]
			c=c+1
		if(s[k]=='L'and x%m!=0):
			l1[x],l1[x-1]=l1[x-1],l1[x]
			c=c+1
		if(s[k]=='R'and (x+1)%m!=0):
			l1[x],l1[x+1]=l1[x+1],l1[x]
			c=c+1	
		for d in range(len(l1)):
			if(l1[d]=="_"):
   				x=d 										
	if(c==len(s)-1):
		print("Puzzle",b,"#")
		n=0
		c1=c1+1
		while(n<len(l1)):
			if(n%m==0):
				print("\n")
			print(l1[n],end=" ")
			n=n+1	
	if(c1==0):
		print("This puzzle has no final configuration")
		print("\n")						                	
	a=input("enter input of next character:")
	if(a=='Z'):
		b=0						
	else:
		d=len(l1)
		b+=1
		del l1[0:d]																			
		c=0		
		c1=0
