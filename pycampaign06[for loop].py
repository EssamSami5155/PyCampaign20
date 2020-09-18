# Todays topics:
    # for loop revise
    # turtle.color()
    # break/continue
    # list in loop


import turtle

a = turtle.Turtle()
for i in range(4):
    a.forward(100)
    a.right(90)
    for j in range(4):
        a.forward(50)
        a.right(90)

turtle.done()