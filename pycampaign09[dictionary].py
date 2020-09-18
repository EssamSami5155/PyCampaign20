# dictionary
my_diction = {}
my_diction = dict()
my_diction = {"mobile":"01","college no":5130}
new_diction = {"blood":"B+","class":10, "mobile":"99"}

my_diction.update(new_diction)
print(my_diction)

for key, value in my_diction.items():
    print(key,value)
    print()