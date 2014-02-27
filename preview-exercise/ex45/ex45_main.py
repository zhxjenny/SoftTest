#-*- coding:utf-8 -*-
import ex45_computer
from ex45_computer import Computer

def MatchtoComputer(userType,computerType):
	
	win =0
	print "Being to match...userType is %s computerType is %s" %(userType,computerType)
	if((userType =="r" and computerType == "r")or((userType =="p" and computerType=="p")or(userType=="s" and computerType=="s"))):
		print " both win,your type is:%s, computer is:%s; input again ,input r,p or s " %(userType,computerType)
		#no win
		win= 0
		return win
	#user win
	if(userType =="r" and computerType == "s")or(userType =="p" and computerType=="r")or(userType=="s" and computerType=="p"):
		print" You win!"
		win="user"
		return win
	#computer win
	if(computerType =="r" and userType == "s")or(computerType =="p" and userType=="r")or(computerType=="s" and userType=="p"):
		print "Computer win"
		win ="computer"
		return win
	return win
	

#begin to run the game; game Type 1: the user win forever; 2:computer win forever;3 true game random
def GameBeginRun( gameType):
	win =0
	
	#GET USER TYPE
	userType=raw_input("please input r or p or s ;r is 'rock',p is 'paper',s is 'scissors'\n.")
	#computer type
	mycomputer =Computer(gameType,userType)
	
	mycomputer.SetComputerType()
	myComputerType=mycomputer.GetComputerType()
	
	
	
	win = MatchtoComputer(userType,myComputerType)
	
	print("game over!\n")
	exit(0)
	
# finger-guessing game
print "welcome to finger-guessing game,let's go!"
print " the game have 3 types;please input 1 or 2 or 3 to select."

user_input=raw_input("please input  1 or 2 or 3:")
ret = GameBeginRun(user_input)
if(ret == "-1"):
	print "Game error"


