the_count =[1,2,3,4,5]
fruits =['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']
# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d"% number
#same as above
for fruit in fruits:
	print "A fruit of type:%s" %fruit
#also we can go through mixed list
for i in change:
	print "I GOT %r" %i
elements=[]
ele=[]
for i in range(0,6):
	print "Adding %d to the list." %i
	#append the list
	elements.append(i)
ele=range(0,6)	
for i in elements:
	print "Element was:%d" %i
for i in ele:
	print "ele is %d" %i