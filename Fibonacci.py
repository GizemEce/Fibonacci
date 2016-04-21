#Gizem Ece Yilmaz

#Contract:number->list
#Purpose: write all fibonacci numbers till n
#Examples: 
# 1->[1,1]
# 2->[1,1]
# 3->[1,1,2,3]
# 4->[1,1,2,3]
# 5->[1,1,2,3,5]

def fibonacci(n):
	new=[]
	a,b=1,1
	if n<=2:
		new.extend([a,b])
	else:
		new.append(1)
		while(b<=n):
			new.extend([b])
		 	a,b = b,a+b
        return new
	   		 

print fibonacci(1)
print fibonacci(2)
print fibonacci(3)
print fibonacci(4)
print fibonacci(10)

