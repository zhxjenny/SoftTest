def myfun(bookcount, booktype, monkeyvalue):
	print "mybookcount is %d, booktype is %d, monkeyvalue is %d\n" %(bookcount,booktype,monkeyvalue)

def myfun2(*args):
	mybookcount,mybooktype,mymonkeyvalue=args
	print "two mybookcount2 is %d, booktype2 is %d, monkeyvalue2 is %d\n" %(mybookcount,mybooktype,mymonkeyvalue)

def myfun3(*args):
	para1,para2,para3,para4,para5=args
	print"para1 is %s para2 is %s para3 is %s para4 is %s para5 is %s\n" %(para1,para2,para3,para4,para5)
	
print "Now we call the function:"
myfun(10,20,100)
myfun2(50,60,70)
myfun3(1,2,3,4,5)