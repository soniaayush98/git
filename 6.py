i=raw_input("enter a word :")
a={}
for x in i :
	if x in a:
		a[x]=a[x]+1
	else:	
		a[x]=1

print a
