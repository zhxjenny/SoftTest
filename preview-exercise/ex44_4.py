class Parent(object):
	def override(self):
		print "Parent override()"
	def implicit(self):
		print "Parent implicit()"
	def altered(self):
		print "parent altered()"
class Child(Parent):
	def override(self):
		print "Child override()"
	
	def altered(self):
		print "Child, before parent altered()"
		super(Child,self).altered()
		print "child,after parent altered()"

dad = Parent()
son= Child()

dad.override()
son.override()

dad.implicit()
son.implicit()

dad.altered()
son.altered()