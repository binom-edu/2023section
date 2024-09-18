import turtle
k = 20

turtle.left(90)
turtle.pendown()
for i in range(3):
    turtle.right(60)
    turtle.forward(k*10)
    turtle.right(60)

turtle.penup()
for x in range(10):
    for y in range(-5, 6):
        turtle.goto(k*x, k*y)
        turtle.dot(5)

turtle.mainloop()