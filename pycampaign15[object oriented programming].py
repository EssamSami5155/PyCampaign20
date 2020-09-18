class Employee:
	RAISE_AMOUNT = 1.05
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+last+"@gmail.com"

	def fullname(self):
		name = self.first + " " + self.last
		return name

	def apply_raise(self):
		self.pay = int(self.pay*Employee.RAISE_AMOUNT)

	@classmethod
	def set_raise_amount(cls,amount):
		cls.RAISE_AMOUNT = amount

	@classmethod
	def form_string(cls,emp_str):
		emp_list = emp_str.split("-") 
		first = emp_list[0]
		last = emp_list[1]
		pay = emp_list[2]
		return cls(first,last,pay)

	@staticmethod
	def is_holiday(day):
		if day.weekday() == 5 or day.weekday == 4:
				return True
		else:
			return False


emp1 = Employee("Essam","Sami",1000)
emp2 = Employee("Ali","Nawaf",990)

import datetime
my_date = datetime.date(2016,8,20)
print(Employee.is_holiday(my_date))


