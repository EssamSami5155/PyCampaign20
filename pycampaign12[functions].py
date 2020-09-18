# Functions

def feb(x):
	if x == 1 or x == 2:
		return 1
	else:
		return feb(x-1) + feb(x-2)

for f in range(1,20):
	print(feb(f))
