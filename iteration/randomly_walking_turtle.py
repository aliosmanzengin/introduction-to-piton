import random
import turtle


def isInScreen(w, t):
    left_bound = -(wn.window_width() / 2)
    right_bound = wn.window_width() / 2
    top_bound = wn.window_height() / 2
    bottom_bound = - wn.window_height() / 2

    x = t.xcor()
    y = t.ycor()
    still_in = True

    if x > right_bound or x < left_bound:
        still_in = False
    if y > top_bound or y < bottom_bound:
        still_in = False

    return still_in


t = turtle.Turtle()
wn = turtle.Screen()
t.speed(0)
t.shape('turtle')
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:  # heads
        t.left(90)
    else:  # tails
        t.right(90)

    t.forward(50)
print("finished")
wn.exitonclick()
