#-*- coding:utf-8 -*-
import ex45_computer
from ex45_computer import Computer
#计算机的手型和用户的手型比较，看输赢
def MatchtoComputer(userType,computerType):
	
	win =0
	print "Being to match...userType is %s computerType is %s" %(userType,computerType)
	
	# no winner
	if((userType =="r" and computerType == "r")or((userType =="p" and computerType=="p")\
	or(userType=="s" and computerType=="s"))):
		print " both win,your type is:%s, computer is:%s; input again ,input r,p or s " %(userType,computerType)
		#no win
		win= 0
		return win
		
	#user win
	if(userType =="r" and computerType == "s")or(userType =="p" and computerType=="r")or\
	(userType=="s" and computerType=="p"):
		print" You win!"
		win="user"
		return win
		
	#computer win
	if(computerType =="r" and userType == "s")or(computerType =="p" and userType=="r")or\
	(computerType=="s" and userType=="p"):
		print "Computer win"
		win ="computer"
		return win
	return win
	

#begin to run the game; game Type 1: the user win forever; 2:computer win forever;3 true game random
def GameBeginRun( gameType):
	win =0
	userTypeError = True
	#GET USER TYPE
	while(userTypeError):
		userType=raw_input("please input r or p or s ;r is 'rock',p is 'paper',s is 'scissors'\n.")
		#computer type
		if(userType !="r" and userType !="s" and userType !="p"):
		
			print "Input error, please input r or s or p. input again\n"
			continue
		else:
			userTypeError = False
			break
	mycomputer =Computer(gameType,userType)

	mycomputer.SetComputerType()
	myComputerType=mycomputer.GetComputerType()
	
	
	
	win = MatchtoComputer(userType,myComputerType)
	
	print("game over!\n")
	exit(0)
	
# finger-guessing game  main begin

print "welcome to finger-guessing game,let's go!\n If you want to leave the game, input 'out' or 'o' "

user_in =True
while (user_in):
	print " the game have 3 types;please input 1 or 2 or 3 to select."
	print "1 the user always win;2 computer always win;3 true match,true game"

	user_input=raw_input("please input  1 or 2 or 3:")
	if((user_input!="1")and(user_input !="2")and(user_input !="3")):
		print "input error;please input again ;please input 1 or 2 or3 \n"
		continue
	if(user_input =="out" or user_input =="o"):
		print "game over; welcome again.bye bye!"
		user_in=False
		break
	ret = GameBeginRun(user_input)
	if(ret == "-1"):	
		print "Game error"
		continue

		


