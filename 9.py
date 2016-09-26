a=int(input("enter an odd number :"))
i=0
b=1
x=1
while (x<=a):
	i=a-x+1
	while (i<a):
		print " ",
		i+=2
	i=a-x+1
	while (b<=i):
		print "*",
		b+=1
	
	while (i<a):
		print " ",
		i+=2
	print ""	
	b=1
	x+=2
	
