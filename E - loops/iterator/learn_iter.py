# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

# An iterable user defined type
class Test:

	# Constructor
	def __init__(self, limit):
		self.limit = limit

	# Creates iterator object
	# Called when iteration is initialized
	def __iter__(self):
		self.x = 10
		return self

	# To move to next element. In Python 3,
	# we should replace next with __next__
	def __next__(self):

		# Store current value of x
		a = self.x

		# Stop iteration if limit is reached
		if a > self.limit:
			raise StopIteration

		# Else increment and return old value
		self.x = a + 1
		return a

val = Test(20)
# Prints numbers from 10 to 15
for i in val:
	print(i)

# Prints nothing
for i in Test(5):
	print(i)
