class Other(object):
	def override(self):
		print "Other override()"
	def implicit(self):
		print "Other implicit()"
	def altered(self):
		print "Other altered()"
		
class Child(object):
	def __init__(self):
		self.other=Other()
	def implicit(self):
		self.other.implicit()
	def override(self):
		print "Child override()"
	
	def altered(self):
		print "Child, before parent altered()"
		self.other.altered()
		print "child,after parent altered()"
		
	
son= Child()

son.override()


son.implicit()


son.altered()