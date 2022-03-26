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

	koptok.goto(x+x1, y+y1)


oyna.mainloop()