import turtle

# turtle is great for beginners
wn=turtle.Screen()
wn.title("Pong by Cody Snell")
wn.bgcolor("black")
# setup as a grid 0,0 center 4 quadrants +400 right -400left +300up -300down
wn.setup(width=800, height=600)
# stops window from updating, speeds up game quite a bit
wn.tracer(0)

# Paddle A
# turle object small t for object name big T for class name
paddle_a = turtle.Turtle()
# sets animation speed not speed of paddle on screen, 0 sets to maximum
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color("white")
# by default Turtle is 20px X 20px multiples by what you stretch by 20x5=100 20x1=20
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# turtles by default draw a line as theyre moving penup prevents that
paddle_a.penup()
# where paddle starts at on screen
paddle_a.goto(-350,0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("white")
ball.penup()
ball.goto(0,0)
#  movement speed 
ball.dx = 0.27
ball.dy = 0.27


# Functions

# ycor is built into turtle module returns y cord and sets into var named y

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
# tells window to listen for keyboard input
wn.listen()
# when user presses w, call on function
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
# for arrow keys use capital Up Down keywords
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# Every game needs a main game loop
# can not mix spaces and tabs stay consistant!!

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking, we want the ball to bounce on borders top/bottom

    if ball.ycor() >290:
        # stops ball at border
        ball.sety(290)
        # reverses the direction
        ball.dy *= -1

    if ball.ycor() < -290:
        # stops ball at border
        ball.sety(-290)
        # reverses the direction
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1