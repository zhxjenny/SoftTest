def add(a,b):
	print "Adding %d +%d" %(a,b)
	return a+b
def subtract(a,b):
	print "subtracting %d-%d" %(a,b)
	return a-b
def multiply(a,b):
	print "multiplying %d*%d" %(a,b)
	return a*b
def divide(a,b):
	print "dividing %d/%d" %(a,b)
	return a/b

def fun1(a,b,c,d):
	print " Now YOU MATH:"
	return( a+(b/c)-d)
print "Let's do some math with just functions!"
age =add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print "Age:%d,Height:%d,Weight:%d,IQ:%d" %(age,height,weight,iq)

#A puzzle for the extra credit, type it in anyway
print "here is a puzzle."

what =add(age,subtract(height,multiply(weight,divide(iq,2))))
print "That becomes:",what,"Can you do it by hand?"
x = int(raw_input('input int'))
print x
y=float(raw_input('input float:'))
print y
print int(y)

z=fun1(100,10,2,5)
print "z is",z