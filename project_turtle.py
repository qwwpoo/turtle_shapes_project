from turtle import Turtle,Screen
import random
sam = Turtle()


sam.hideturtle()
window = Screen()
window.bgcolor('black')
window.setup(1.0,1.0)
color = ['white','green','red','blue','orange','pink']
shapes = ['turtle','circle','square']


while True:
 name = window.textinput('هلا بك','اكتب اسم المشروع رجأ')
 sam.pensize(random.randint(5,25))
 sam.color(random.choice(color))
 sam.shape(random.choice(shapes))

 if name == 'square'or name == 'مربع':

  for _ in range(4):
   sam.forward(50)
   sam.left(90)

 elif name == 'triangle' or name == 'مثلث':

  for _ in range(3):
   sam.forward(50)
   sam.left(120)
 elif name == 'circle' or name == 'دائره':
  sam.circle(50)
 elif name == 'exit' or name == 'خروج':
  window.clearscreen()
  break 
  
window.bgcolor('pink')
sam.write('press any key to exit\n',font = ('arial',40,'bold'),align = 'center')
sam.write('اضغط في اي مكان لكي تخرج',font = ( 'arial',30,'normal'),align = 'center')
















window.exitonclick()