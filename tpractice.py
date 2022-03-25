import turtle

vn = turtle.Screen()
vn.title = "'Tic Tac Toe' Av Nicolai"
vn.tracer(0)

turtle.speed(2)
 
for i in range(4):
    turtle.forward(300)
    turtle.left(90)

turtle.penup()
turtle.goto(0,100)
turtle.pendown()
 
turtle.forward(300)
 
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
 
turtle.forward(300)
 
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
 
turtle.left(90)
turtle.forward(300)
 
turtle.penup()
turtle.goto(200,0)
turtle.pendown()
 
 
turtle.forward(300)

turtle.done()

        

