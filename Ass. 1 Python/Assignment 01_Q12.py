import turtle
t= turtle.Turtle()


def draw_square (t,side_length):
    for i in range (4):
        t.forward(side_length)
        t.left(90)
    t.up()
    t.forward(5)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.down()


draw_square(t,200)
draw_square(t,190)
draw_square(t,180)
draw_square(t,170)
draw_square(t,160)
draw_square(t,150)
draw_square(t,140)
draw_square(t,130)
draw_square(t,120)
draw_square(t,110)



draw_square=turtle.Screen()
draw_square.setup(startx =0, starty=0)
