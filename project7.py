import turtle
turtle.Screen().bgcolor("Orange")
sc = turtle.Screen()
sc.setup(400,300)
turtle.title("Welcome to Turtle Window")
board = turtle.Turtle()
for i in range(6):
    board.forward(100)
    board.left(60)
    i=i+1
turtle.done()
