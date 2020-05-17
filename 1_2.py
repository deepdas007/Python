# USING THE TURTLE
import turtle 

wn = turtle.Screen() 
wn.bgcolor("black") 

alex = turtle.Turtle() 
alex.color("white") 

alex.pensize(10)
alex.speed(1.5)
alex.up()
for _ in range(15):
	alex.forward(20)
	alex.stamp()
	alex.right(24)

deep = turtle.Turtle()
deep.color("red")
deep.pensize(10)
deep.speed(2)
deep.up()
deep.left(90)
deep.forward(40)
deep.stamp()
deep.right(90)
for _ in range(15):
	deep.forward(20)
	deep.stamp()
	deep.right(24)

neha = turtle.Turtle()
neha.color("blue")
neha.pensize(10)
neha.speed(2)
neha.up()
neha.left(90)
neha.forward(100)
neha.stamp()
neha.right(90)
for _ in range(15):
	neha.forward(20)
	neha.stamp()
	neha.right(24)

wn.exitonclick() #END THE PROGRAM ON THE LET CLICK OF THE MOUSE ON THE SCREEN