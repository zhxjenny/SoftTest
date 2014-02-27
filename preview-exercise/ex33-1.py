i=0
number=[]
maxnumber=20
while i<maxnumber:
	print "At the top i is %d" %i
	number.append(i)
	i=i+3
	print "Numbers now:",number
	print "At the bottom i is %d" %i
print "The number:"

for num in number:
	print num
