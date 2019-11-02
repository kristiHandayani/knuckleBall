import turtle

# define ball atribute
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Knuckle Ball Simulator")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)

# define ball position before the kick
ball.goto(-200, -200)

# define ball movement 
ball.dy = 6
ball.dx = 4

# slow down the ball
gravity = 0.1

while True:
    # change ball position
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() < -200:
        ball.dy *= -1

    # assume the ball already in goal post
    if ball.xcor() >300:
        break

wn.mainloop()