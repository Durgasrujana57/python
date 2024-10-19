class cons:
	def __init__(self):
		self.greet="good morning"
	def display(self):
		print("msg = " , self.greet)
	def __del__(self):
		print("object destroyed")
dc=cons()
dc.display()
print(dc)
del dc		
