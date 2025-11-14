from turtle import Turtle, Screen


cat = Turtle()
cat.color('red')
cat.speed('fastest')

window = Screen()
window.bgcolor('black')
window.setup(width=1.0, height=1.0)  


def go(a, p):
    cat.penup()
    cat.goto(a, p)
    cat.pendown()


def draw_square_pattern():
    go(-300, 200)
    for _ in range(30):
        for _ in range(4):
            cat.forward(50)
            cat.left(90)
        cat.left(25)


def draw_weird_shape():
 cat.color('orange')
 go(-200, 0)
 for _ in range(50):
    for _ in range(3):
       cat.left(90)
       cat.forward(90)
    cat.left(25)
 		

def draw_triangle_pattern():
 cat.color('yellow')
 go(200, 200)
 for _ in range(50):
    for _ in range(3):
      cat.left(120)
      cat.forward(90)
    cat.left(25)
 		


def draw_circles():
 cat.color('blue')
 go(200, -200)
 for _ in range(50):
   for _ in range(50):
     cat.left(7.2)
     cat.forward(10)
   cat.left(10)
 	
go(-200,-200)
cat.circle(30)

draw_square_pattern()
draw_weird_shape()
draw_triangle_pattern()
draw_circles()

window.exitonclick()
