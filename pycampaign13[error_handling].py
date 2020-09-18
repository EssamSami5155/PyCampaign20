# Error Handling

def K2F(temp):
	assert (temp >= 0),"colder than absolute zero"
	far = ((temp-273.25)*1.8)+32
	return far

print(K2F(-3))
