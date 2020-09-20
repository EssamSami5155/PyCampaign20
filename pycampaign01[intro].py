# Before reading this Download Python interpreter in your device.
    # pydroid3 for android
    # pythonista for ios
    # python 3 for windows/mac/linux (link: https://www.python.org/downloads/)
    



# 1. Intro with Python
# --> Programing language give us opportunity to contact with devices.
# --> Python is currently the number one famous programming language.
# --> it is used for Artificial Intelligence, Web Development, Software Enginnering and many more.

# first line of code - this is called comment (have to start with #, doesnt inturupt the programme)

# print-it is a command/function/method
# Function/command is also known as method. Function and command are same.
# But method is little different.
# Method is a special kind of function which belongs to a class (will discuss later). 

# "hello world"-it is string of text.
# print command prints a message on the screen.
print ("hello world")
print ('I am Shawki')

# 2. Basic DataTypes
# String - str(short form) - ex. "Hello" (Note the quotes)
# Integer - int - ex. 34 (without ")
# float - float - ex. 45.34 (decimal)
# Boolean - bool - ex. True , False (Note capital T and F)

# 3. How to use Functions/Commands
# print the type of an object.
type("Hello") # wont print anything
print(type("Hello"))
print(type(45))
print(type("45.67"))# Note string
print(type(67.777))
print(type(True))

# print available functions from directory
print(dir(str))

# print help from python
print(help(str))
print(help(len))

# print the total number of character in a string.
print(len("Ahammad Shawki")) # Note len means length

# --> there are tons of functions in Python.

#4. Printing
print("I am Shawki")
# printing in new line.
print("first line")
print("second line")
# or,
print("First line \nSecond line") # Note \(backslash is known as escape command)
#\n means newline
#\t means tab
print("I am far \t away")
# we can use both double quotes and single quotes for string.
print("hello")
print('hello')
# But it is good to stick with one. sometimes we need to use quotes in our string.
print("I can't swim") # this is good but,
print('I can't swim) # this will give us an error. Because , python will think that the string is ended before t.
# in that case we can use escape command to tell python that we are not end yet.
print('I can\'t swim')
# what if we need a backslash in our string.
print("I can\t swim") # python will think \t is tab, it wont print the backslash.
# So, we can add another backslash before the bacjkslash/
print("I can\\t swim") # what we expected.

#5. Slicing
# Index : Characters Location in string. Starts with 0. Also possible negative indexing.
# "Hello World"
#  012345678910
#  -11-10-9-8-7-6-5-4-3-2-1

# variable (will discuss later)
a = "Hello World" # a stores the value of "Hello World"
print(a[0]) # print H
print(a[-2]) # print l
print(a[0:4]) # print Hell (Because range in python is exclusive)
# So it will print up to 4, not including 4.
print(a[0:5]) # print Hello
print(a[-11:-6]) # print Hello
print(a[0:-6]) # print Hello
print(a[3:]) # print from l to the last
print(a[:8]) # print from first to o
print(a[0::2]) # step is 2, print first to last but gaps 1 letter in each step
print(a[0::3]) # step is 3, print first to last but gaps 2 letter in each step
print(a[-1::-1]) # print the whole message reversely.
      
