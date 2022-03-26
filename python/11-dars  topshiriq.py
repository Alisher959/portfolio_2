from turtle import Turtle, Screen, circle
oyna = Screen()
oyna.title('Mening oynam')

chiziq = Turtle()
chiziq.color('blue')
chiziq.pensize(5)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(300, 300)
chiziq.down()
chiziq.goto(300, -300)
chiziq.goto(-300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)

green = Turtle()
green.color('green')
green.pensize(5)
green.speed(0)
green.hideturtle()
green.up()
green.goto(-270, -270)
green.down()
green.goto(-270, -300)
green.goto(-200, -300)
green.goto(-200, -270)
green.goto(-270, -270)


koptok = Turtle()
koptok.shape('circle')
koptok.color('red')
koptok.up()
koptok.goto(30, 60)
x1=2
y1=3
while True:
	x, y = koptok.position()
	if x+x1 >= 300 or x+x1 <= -300:
		x1=-x1
	if y+y1 >= 300 or y+y1<= -300:
		y1=-y1
	if x+x1 >= -270 and x+x1 <= -200  and y+y1 >=-300 and y+y1 <=-270 :
		break


oyna.mainloop()