# ex09.py

import turtle as t
from random import random

t.shape('turtle')

# 거북이(3시 방향)
# 
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# for i in range(100):
#     t.forward(i * 2)
#     t.right(60)
#     t.forward(i * 3)
#     t.left(40)

# t.pensize(10)
# t.color('red')
# t.circle(100)
# t.fillcolor('yellow')
# 
# t.reset()

# import random
# 
# t.speed(10)
# 
# for i in range(100):
#     x = int(random.random() * 300)
#     y = int(random.random() * 300)
#     size = int(random.random() * 100)
#     t.up()
#     t.goto(x, y)
#     t.down()
#     t.circle(size)


ninja = t.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()

input('')


















