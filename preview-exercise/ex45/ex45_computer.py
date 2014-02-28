#-*- coding:utf-8 -*-
#computer handtype
import random

#user win type
ComputerList1={"r":"s","p":"r","s":"p"}
#computer win type
ComputerList2={"r":"p","p":"s","s":"r"}
#random type,true game
ComputerList3=["r","s","p"]
class  Computer():
	def __init__(self,gametype,userHandtype):
		self.iGametype=gametype
		self.iuserHandtype=userHandtype
		self.computerHandType="3"
	
	#set the computer type ,based on gametype and userHandtype
	def SetComputerType(self):
		print "The computer is thinking..."
		if self.iGametype=="1":
			self.computerHandType=ComputerList1[self.iuserHandtype]
		if self.iGametype=="2":
			self.computerHandType=ComputerList2[self.iuserHandtype]
		if self.iGametype=="3":
			#生成 1 到 3的随机整数
			num=random.randint(1,3)
			print "num is %d",num
			self.computerHandType=ComputerList3[num-1]
		
			
	def GetComputerType(self):
		print "The computer is out hand..."
		print "The computer is %s\n" % self.computerHandType
		return self.computerHandType
	