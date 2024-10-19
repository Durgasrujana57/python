class Principal:
	def Principal(self):
		print("I am principal")
class Teacher(Principal):
	def Teacher(self):
		print("I am teacher")
class Student(Teacher):
	def Student(self):
		print("I am student")
d=Student()
d.Principal()
d.Teacher()
d.Student()
		
