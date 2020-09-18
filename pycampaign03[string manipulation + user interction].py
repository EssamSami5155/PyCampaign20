# manipulate the contents of variables.

# lower, upper, swapcase are different string functions.

message="Hello world"
print(message.swapcase()) # change cases.
print(message.lower()) # all letter is in lower case.
print(message.upper()) # all letter is in upper case.
print(message.capitalize()) # capitalize the first letter of the sentence.
print(message.title()) # capitalize the first letter of every word in the string.
print(message.replace("Hello","hi") )# replace the word after comma to the place of the word before comma.
print(message.find("world")) # tells us the position of the word. 
# the number which comes to the output means the characters before the word is that number.
# we can also tell python where to start and where to end. they are going to be the 2nd and 3rd arguement.
print(message.find("l",4,-1))
print(message.count("o")) # count the number of the letter.
print("       dhaka        ".strip()) # ignore the blank space.
print("       dhaka        ".rstrip()) # ignore the blank space of right side.
print("       dhaka        ".lstrip()) # ignore the blank space of left side.
# we can also use specific character to remove by adding another arguement in those above 3 methods.
print("kkkkkkkkkkkkkk foo kkkkkkkkkkkkkk".strip("k"))
print(message.startswith("H")) # gives a boolean. if a string starts with the character or not.
print(message.endswith("d")) # gives a boolean. if a string ends with the character or not.


# Example-
name=input("what is your name?")
country=input("which country do you live in?")
country=country.upper()
print(name+" lives in "+country+".")

# when we write down a function we can watch a pop up list. that's called intelliSense.
# Visual Studio will suggest possible functions we can call automically after we type any word.
# we can also press ctrl+space to launch intelliSense.

# programmers do not memorize all functions.
# so how do programmers find them when they need them?-
# 1.intellisense, 2.documentation, 3.internet searches.


# asking user to input number 

# there are functions to convert from one datatype to another.
# they are called "casting datatypes" or "datatype conversion"-
# int(value)       converts to an integreter.
# long(value)      converts to a long integreter.
# float(value)     converts to a floating number.  (i.e.  a number that can hold decimal places)
# str(value)       converts to a string. 
# bool(value)      converts to boolean.

a=input("enter a number")
b=input("enter another number")
answer=int(a)+int(b)
print(answer)

# how to find the type of a variable?
# we can use type function
c="Shawki"
print(type(c))
