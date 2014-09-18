class Security(object):
	"""docstring for Security"""
	def __init__(self, arg):
		super(Security, self).__init__()
		self.arg = arg

class Stock(Security):
	"""docstring for Stock"""
	def __init__(self, arg):
		super(Stock, self).__init__()
		self.arg = arg

class Option(Security):
	"""docstring for Option"""
	def __init__(self, arg):
		super(Option, self).__init__()
		self.arg = arg

class Bond(Security):
	"""docstring for Bond"""
	def __init__(self, arg):
		super(Bond, self).__init__()
		self.arg = arg
		

class OtherSecurity(object):
	"""docstring for OtherSecurity"""
	def __init__(self, arg):
		super(OtherSecurity, self).__init__()
		self.arg = arg
