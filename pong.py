import turtle
import os 
import time
import platform

# if on windows import winsound
if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("winsound module not available")

# turtle is great for beginners
wn=turtle.Screen()
wn.title("Pong by Cody Snell")
wn.bgcolor("black")
# setup as a grid 0,0 center 4 quadrants +400 right -400left +300up -300down
wn.setup(width=800, height=600)
# stops window from updating, speeds up game quite a bit
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

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

ball_1 = turtle.Turtle()
ball_1.speed(0)
ball_1.shape('circle')
ball_1.color("white")
ball_1.penup()
ball_1.goto(0,0)
#  movement speed
ball_1.dx = 0.27
ball_1.dy = 0.27

ball_2 = turtle.Turtle()
ball_2.speed(0)
ball_2.shape('circle')
ball_2.color("blue")
ball_2.penup()
ball_2.goto(0,0)
ball_2.dx = -0.27
ball_2.dy = -0.27

ball_3 = turtle.Turtle()
ball_3.speed(0)
ball_3.shape('circle')
ball_3.color("red")
ball_3.penup()
ball_3.goto(0,0)
ball_3.dx = 0.37
ball_3.dy = 0.37

ball_4 = turtle.Turtle()
ball_4.speed(0)
ball_4.shape('circle')
ball_4.color("purple")
ball_4.penup()
ball_4.goto(0,0)
ball_4.dx = -0.4
ball_4.dy = -0.4

balls = [ball_1, ball_2, ball_3, ball_4]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("You: 0  The AI: 0", align="center",font=("Courier", 24, "normal"))

# Functions

# ycor is built into turtle module returns y cord and sets into var named y

def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def play_sound(sound_file, time = 0):
    # Windows
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # Linux
    elif platform.system() == "Linux":
        os.system("aplay -q {}&".format(sound_file))
    # Mac
    else:
        os.system("afplay {}&".format(sound_file))

#Keyboard binding
# tells window to listen for keyboard input
wn.listen()
# when user presses w, call on function
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
# gives two options to play
wn.onkeypress(paddle_a_up, "Up")
wn.onkeypress(paddle_a_down, "Down")
# for arrow keys use capital Up Down keywords
# commented out for AI 
# wn.onkeypress(paddle_b_up, "Up")
# wn.onkeypress(paddle_b_down, "Down")



# Every game needs a main game loop
# can not mix spaces and tabs stay consistant!!

# Main game loop
while True:
    wn.update()

    for ball in balls:
        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)



        # border checking, we want the ball to bounce on borders top/bottom and paddle to stop 

        if paddle_a.ycor() > 250:
            paddle_a.sety(250)
        if paddle_a.ycor() < -250:
            paddle_a.sety(-250)

        if ball.ycor() >290:
            # stops ball at border
            ball.sety(290)
            # reverses the direction
            ball.dy *= -1
            # sounds file have to be in same folder for this setup  adding & at the end prevents game from freezing while sound plays
            play_sound("boing.wav")

        if ball.ycor() < -290:
            # stops ball at border
            ball.sety(-290)
            # reverses the direction
            ball.dy *= -1
            play_sound("boing.wav")



        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            score_a += 1
            # pen.clear erases whats written on screen
            pen.clear()
            pen.write("You: {}  The AI: {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))
            play_sound("ball_lost.wav")

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("You: {}  The AI: {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))
            play_sound("ball_lost.wav")



        # paddle and ball collision

        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            play_sound("boing.wav")
            ball.dx *= -1
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            play_sound("boing.wav")
            ball.dx *= -1
        


#  AI player

    closest_ball = balls[0]
    for ball in balls: 
        if ball.xcor() > closest_ball.xcor():
            closest_ball = ball

        if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 17:
            paddle_b_up()

        elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 17:
            paddle_b_down()


# deciding a winner 

    if score_a == 10:
        pen.clear()
        pen.write("You Won!", align="center",font=("Courier", 24, "normal"))
        play_sound("win.wav")
        for ball in balls:
            # reset the balls
            ball.goto(0,0)
        paddle_a.goto(-350,0)
        paddle_b.goto(350,0)
        wn.update()
        time.sleep(5)
        score_a = 0
        score_b = 0
        pen.clear()
        pen.write("You: {}  The AI: {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))

    if score_b == 10:
        pen.clear()
        pen.write("The AI Wins!", align="center",font=("Courier", 24, "normal"))
        play_sound("game_over.wav")
        for ball in balls:
            # reset the balls
            ball.goto(0,0)
        paddle_a.goto(-350,0)
        paddle_b.goto(350,0)
        wn.update()
        time.sleep(5)
        score_a = 0
        score_b = 0
        pen.clear()
        pen.write("You: {}  The AI: {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))
wn.mainloop()


