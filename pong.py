import turtle
import random

window = turtle.Screen()
window.title("Pong Game")
window.setup(width=600, height=400)
window.bgcolor("black")

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.color("white")
left_paddle.penup()
left_paddle.goto(-250, 0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(250, 0)

ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

def paddle_a_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def paddle_a_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Set up key bindings for left paddle
window.listen()
window.onkeypress(paddle_a_up, "Up")
window.onkeypress(paddle_a_down, "Down")


while True:
    right_paddle.sety(ball.ycor())

    # Update the ball position
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collisions with the top and bottom walls
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Check for collisions with the left and right walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1

    # Check for collisions with the paddles
    if ball.xcor() > 240 and ball.distance(right_paddle) < 50 or ball.xcor() < -240 and ball.distance(left_paddle) < 50:
        ball.dx *= -1

    
