class matrix:
	def __init__(self,rows=0,columns=0):
		self.rows = rows
		self.columns=columns
	def __str__(self):	
			global a		
			a =[[0 for x in range(self.columns)]for y in range(self.rows)]
			d=0
			for x in range(int(self.rows)):
				while(d<((x+1)*self.columns)):
					a[x][d-x*self.columns]=d
					d+=1
			for y in range(int(self.rows)):
				for x in range(int(self.columns)):
					print a[y][x],
				print 
			return "%d rows and %d columns"%(self.rows,self.columns)
	def __getitem__(self,(x,y)):
		
		return a[x][y]
	
		
		
		

a=int(input("no. of rows : "))
b=int(input("no. of columns : "))
f=matrix(a,b)
print f
c=int(input("no. of row : "))	
d=int(input("no. of column : "))
d-=1
c-=1
print f[c,d]
		
