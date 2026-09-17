from turtle import*

bgcolor("black")
speed(0)
hideturtle()

for i in range(160):
    color("white")
    circle(i)
    color("green")
    circle(i*0.8)
    right(3)
    forward(3)
done()