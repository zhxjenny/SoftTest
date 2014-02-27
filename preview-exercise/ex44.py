#-*- coding: utf-8 -*-
class Parent(object):
	def override(self):
		print "PARENT OVERRIDE（）"
class Child(Parent):
	def override(self):
		print "Child override()"
	
dad=Parent()
son=Child()

dad.override()
son.override()
