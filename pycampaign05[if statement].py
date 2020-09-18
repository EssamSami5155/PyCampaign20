# Todays Topic:
    # if Statement
    # Loop

#---------- code starts from here ---------
# repeat
    # for - tell python how many times we want to repeat
    # while- repeats until certain condition is True

user = int(input("Enter total repeats: "))


a = 0
b = 1
for step in range(user):
    a , b = b, a+b
    print(a)

