# if statement

answer = input("Do you buy a ice-cream for me? (yes/no)\n")
if answer =="yes": # if statement allows us to specify code that only executes if a specific condition is true.
    print("Of course. Why not?") # we have to press TAB before writing down print command.
if answer =="no": # we have to write a colon(:) after the condition.
    print("No. I don't have enough money.")
print("Have a nice day.")

# When we use if statement-
# comparisons-
# ==    equal to
# !=    not equal to
# <     less than
# >     greater then
# <=    less than or equal to
# >=    greater than or equal to 
# is    object identity

# But sometimes the user may not answer as our thought. In this case we need to manipulate the code. EXP-
team=input("what is your favourite team?\n")
if team.upper()=="REAL MADRID":
    print("That's my favourite team too!!")

# if with numbers
deposit=input("How much you want to diposit?\n")
if int(deposit) > 100 :
    print("Congratulation! you have became our special member.")
print("Have a nice day!")

# else statement
deposit=input("How much you want to diposit?\n")
if int(deposit) > 100 :
    print("Congratulation! you have became our special member.")
else: # else code is only executed if the condition is not true.
    print("Thanks for your deposit.")
print("Have a nice day!")

# boolean variables. 
# We use boolean variables to remember if a condition is true or false.
# coders call it flag.

# Initialize the variable to fix the error.
freetoaster=False

deposit=input("How much you want to diposit?\n")
if int(deposit) > 100 :
    # set the boolean variable freetoaster is true.
    freetoaster=True   
# if the variable freetoster is true the print statement is execute-
if freetoaster:
    print("enjoy your toaster!")

# what is the difference between is and == ?
# is means we are checking if both variables have same id or not. id is the number of the objects in memory.
# == means we are checking if both variables contain same values or not.
a=[1,2,3]
b=[1,2,3]
print(id(a))# we can print a variable's id by "id" function.
print(id(b))
print(a==b)# true
print(a is b)# false
# a and b doesn't have same id.
# their id are save as different object in the memory.

# can anytime two different variables id be same?
# yes.
# exp- 
a=[1,2,3]
b=a
print(id(a))
print(id(b))
print(a==b)# true
print(a is b)# true

# there are some argument which python evaluates to false.
# False Values-
#   False (keyword)
#   None  (keyword)
#   zero(0) of any numeric type.
#   any empty sequences. for example-"",(),[]
#   any empty mapping. for example-{}

# turnery operator
# we can use if else statement when we are initializing a variable. it is called teunery operator.
# this is pretty much like lambda function.
a=101
b=200 if a==100 else 300
print(b)

# we can allso use else statement with loop.
# we dont have to use if statement before.
for i in range(5):
    print(i)
else:
    print("Done")
# this else code will execute after our looping get stopped.

# we can also use  else statement after error handling.
# it will execute if certain except statement becomes False.
my_file = "/temp/test.txt"

try:
    f=open(my_file,"r")
except IOError as e:
    print("File cannot be accessed")

else:
    with f:
        print(f.read())

# all() and any() function.
# all() and any() function takes an iterable as an arguement.
# all() returns true if all the values of that iterable is true, otherwise false.
# any() returns true if any of the values of that iterable is true, otherwise false.
if all([True,True,True,False]):
    print("Ok")
else:
    print("no")

if any([True,False,False,False]):
    print("ok")
else:
    print("no") 




# using if statement in complex situation

# elif
country= input("Where are you form?\n").upper()
if country=="ENGLAND":
    print("Hello!")
elif country=="GERMANY":# elif allows us to check for different values. It means else-if.
    print("Gutan Tag!")
elif country=="FRANCE":
    print("Bonjour!")
elif country=="MEXICO":
    print("Ola Amigo!")
elif country=="INDIA":
    print("Namaste!")
else:
    print("Hey!")

# The code will run 1st condition first.If it is true, then it doesn't run the other condition.
# If it is not true then it run the 2nd conditon.
#exp-

deposit=int(input("How much you want to deposit?\n"))
if deposit> 1000:
    print("You got a new TV!")
elif deposit> 100:
    print("You got a new toaster!")
else:
    print("You got a new mug!")
print("Have a nice day!")


# and/or
# and statement will only execute if every condition is True.

wonlottery=False
bigwin=False
lottery=input("Have you won a lottery?(yes/no)\n").lower()
if lottery==("yes"):
    wonlottery=True
    amount=int(input("How much have you won?\n"))
    if amount > 1000000 :
        bigwin=True
    else:
        bigwin=False
if wonlottery and bigwin:
    print("You can retire.")
else:
    print("You can\'t retire.")

# or statement executes is either one codition is true.

saturday=False
sunday=False
day=input("What day is today?\n").lower()
if day=="saturday":
    saturday=True
else:
    saturday=False
if day=="sunday":
    sunday=True
else:
    sunday=False
if saturday or sunday:
    print("Today is holiday.")
else:
    print("Today is working day.")

#combining multiple "and"/"or" command in a single if statement.

month=input("which month is it?\n").lower()
if month=="september" or month=="november" or month=="june" or month=="april":
    print("There 30 days in this month.")
elif month=="february":
    print("There are 28 days in this month.")
else:
    print("There are 31 days in this month.")


favmovie=input("What is your favourite movie?\n").lower()
favbook=input("What is your favourite book?\n").lower()
favpast=input("What is your favourite pastime?\n").lower()
if favmovie=="avenzers" and favbook=="harry potter" and favpast=="playing football":
    print("We must hang out!")
else:
    print("I appreciate your choice.")

# Combining and/or in a single statement.
# "and" statement will run first between "and"/"or".
# we need to put () to separate conditions.

favs=input("What is your favourite sport?\n").lower()
favt=input("What is your favourite team?\n").lower()
if favs=="football"  and (favt=="brazil" or "real madrid"):
    print("Great choice. Best team of all time.")
else:
    print("Worst choice. Get out from my code.")

# we can do the same operation by using flag(boolean variables)
football=False
team=False
favs=input("What is your favourite sport?\n").lower()
if favs=="football":
    football=True
else:
    football=False
favt=input("What is your favourite team?\n").lower()
if favt=="brazil" or favt=="real madrid":
    team=True
else:
    team=False
if football and team:
     print("Great choice. Best team of all time.")
else:
    print("Worst choice. Get out from my code.")

# nesting if statement inside each other
# nested statement will only execute if the first statement is true.

monday=False
coffee=False
day=input("What day is today?\n").lower()
if day=="monday":
    monday=True
    drink=input("Do we have any fresh coffee?\n").lower()
    if drink=="yes":
        coffee=True
        print("That\'s what I needed.")
    else:
        coffee=False
    if not coffee:
        print("Go buy a coffee!")
        print("I hate mondays.")
print("Now we can start work.")

# (simmilar to elif statement)
# using nested if statement instead of elif statement.
a=9
b=5
if a < b:
    print("a is less than b")
else:
    if a == b:
        print("a is equals to b")
    else:
        print("a is greater than b")

# making bmi calculator using if statement.
name =input("enter your name: ").capitalize()
height_m =float(input("enter your height in metre: "))
weight_kg =float(input("enter your weight in kilogram: "))

bmi=weight_kg/(height_m**2)
print("bmi: ")
print(bmi)

if bmi < 25:
    print(name+" is not overweight.")
else:
    print(name+" is overweight.")

