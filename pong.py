import turtle

# turtle is great for beginners
wn=turtle.Screen()
wn.title("Pong by Cody Snell")
wn.bgcolor("black")
# setup as a grid 0,0 center 4 quadrants +400 right -400left +300up -300down
wn.setup(width=800, height=600)
# stops window from updating, speeds up game quite a bit
wn.tracer(0)




# Every game needs a main game loop
# can not mix spaces and tabs stay consistant!!


# Main game loop
while True:
    wn.update()



