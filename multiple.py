class Name:
	name=" "
	def name(self):
		print(self.name)
class Surname:
	surname=" "
	def surname(self):
		print(self.surname)
class Fullname(Name,Surname):
	def fullname(self):
		print("Name :",self.name)
		print("surname:",self.surname)
s=Fullname()
s.name="Durga srujana"
s.surname="chintakula"
s.fullname()		
