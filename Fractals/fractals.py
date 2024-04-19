import turtle
import random
window = turtle.Screen()
window.setup(600, 600)

def koch_curve(t, depth, size):
    if (depth == 1):
        t.pencolor((random.randrange(50, 255), random.randrange(0, 25), random.randrange(50, 250)))
        t.fd(size)
    else:
        koch_curve(t, depth-1, size)
        t.rt(60)
        koch_curve(t, depth-1, size)
        t.lt(120)
        koch_curve(t, depth-1, size)
        t.rt(60)
        koch_curve(t, depth-1, size)
        

raphael = turtle.Turtle()
raphael.pu()
raphael.goto(-295, 0)
raphael.pd()
window.colormode(255)
#koch_curve(raphael, 4, 10)

def triangle(t, size):
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)
    
def hypotenuse(t, size):
    t.lt(45)
    t.fd(size)
    t.bk(size)
    t.rt(45)

def square(t, size):
    t.lt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(180)
         
#square(raphael, 20)
def sierpinski(t, depth, size, scale_factor=1):
    if depth == 1:
        square(t, size)
        hypotenuse(t, size * (2 ** (1/2)))
    else:
        sierpinski(t, depth-1, size/2)
        t.fd(size/2)
        sierpinski(t, depth-1, size/2)
        t.lt(90)
        t.fd(size/2)
        t.rt(90)
        sierpinski(t, depth-1, size/2)
        t.rt(180)
        t.fd(size/2)
        t.rt(180)
        sierpinski(t, depth-1, size/2)
        t.rt(90)
        t.fd(size/2)
        t.lt(90)

michelangelo = turtle.Turtle()
michelangelo.pu()
michelangelo.goto(-295, 0)
michelangelo.pd()
#sierpinski(michelangelo, 3, 200)

def tree(t, depth, size, angle):
    if depth == 0:
        t.fd(size)
        t.circle(3)
        t.bk(size)
    else:
        r = random.randrange(1, 3)
        if r == 1:
            angle = angle * 0.75
        elif r == 2:
            angle = angle * 1.2
        elif r == 3:
            angle = angle * 1.50
        t.fd(size)
        t.rt(angle)
        tree(t, depth-1, size * 0.75, angle)
        t.lt(2 * angle)
        tree(t, depth-1, size * 0.75, angle)
        t.rt(angle)
        t.bk(size)
        


leonardo = turtle.Turtle()
leonardo.lt(90)
leonardo.pd()
tree(leonardo, 6, 70, 20)

window.exitonclick()
