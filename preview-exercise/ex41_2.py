#-*-coding：utf-8-*-
#Animal is a object
class Animal(object):
	pass

#dog class define
class Dog(Animal):
	def __init__(self,name):
		#define name
		self.name=name
#cat class define
class Cat(Animal):
	def __init__(self,name):
		self.name=name
#person
class Person(object):
	def __init__(self,name):
		#name
		self.name=name
		#Person has a pet of some kind
		self.pet =None
class Eployee(Person):
	def __init__(self,name,salary):
		#调用父类的初始化方法来作为自己的初始化方法
		super(Employee,self).__init__(name)
		
		self.salary=salary

class Fish(object):
	pass
class Salmon(Fish):
	pass
class Halibut(Fish):
	pass

#run the app , new a object
rover=Dog("Rover")
print rover.name
statan=Cat("Satan")
print statan.name
mary=Person("Mary")
print mary.name
