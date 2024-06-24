import turtle
import numpy
import sympy
import sympy.integrals
import sympy.integrals.transforms

screen = turtle.Screen()
screen.setup(450, 450)

turtle.speed("fastest")
turtle.hideturtle()
turtle.tracer(False)
turtle.penup()
turtle.pencolor('black')

canvas_step = 20.0
canvas_length = 10.0

graph_accuracy = 0.01

is_empty = True

def canvas():
    turtle.pendown()
    angle = 0
    while angle < 360:
        turtle.setpos(0, 0)
        turtle.setheading(angle)

        for i in range(int(canvas_length)):
            turtle.pendown()
            turtle.setheading(angle)
            turtle.forward(canvas_step)
            turtle.setheading(angle + 90)
            turtle.pencolor('#D3D3D3')
            turtle.forward(canvas_length * canvas_step)
            turtle.back(canvas_length * canvas_step * 2)
            turtle.forward(canvas_length * canvas_step)
            turtle.pencolor('black')
            if i < canvas_length - 1:
                turtle.forward(5)
                turtle.back(10)
                turtle.forward(5)
        
        if angle < 180:
            turtle.setheading(angle + 135)
            turtle.forward(10)
            turtle.back(10)
            turtle.setheading(angle + 225)
            turtle.forward(10)
            turtle.back(10)
        angle += 90
    turtle.penup()

def argument(arg, func_type):
    return float(func_type.subs(x, arg))

def graph_visualiser(func_type):
    global is_empty
    turtle.pencolor('blue')
    turtle.pensize(2)
    for _x in numpy.arange(-canvas_length, canvas_length, graph_accuracy):
        try:       
            _y = argument(_x, func_type)
            if abs(_y) < canvas_length:
                if argument(_x + graph_accuracy, func_type) > canvas_length:
                    _y = canvas_length
                    turtle.pendown()
                    turtle.setpos(_x * canvas_step, _y * canvas_step)
                    turtle.penup()
                    continue
                if argument(_x + graph_accuracy, func_type) < -canvas_length:
                    _y = -canvas_length
                    turtle.pendown()
                    turtle.setpos(_x * canvas_step, _y * canvas_step)
                    turtle.penup()
                    continue
                turtle.setpos(_x * canvas_step, _y * canvas_step)
                turtle.pendown()
                is_empty = False
            else:
                if argument(_x + graph_accuracy, func_type) < canvas_length and argument(_x + graph_accuracy, func_type) > 0:
                    #turtle.pencolor('red')
                    _y = canvas_length
                    turtle.setpos(_x * canvas_step, _y * canvas_step)
                    turtle.pendown()
                    #print("RED")
                    continue
                if argument(_x + graph_accuracy, func_type) > -canvas_length and argument(_x + graph_accuracy, func_type) < 0:
                    #turtle.pencolor('green')
                    _y = -canvas_length
                    turtle.setpos(_x * canvas_step, _y * canvas_step)
                    turtle.pendown()
                    #print("GREEN")
                    continue
        except:
            print(is_empty)
            continue
    if is_empty == True:
        raise ValueError("invalid function")
    turtle.penup()

def intergration(point1, point2):
    turtle.pencolor("red")
    turtle.pensize(1)
    turtle.setpos(point1 * canvas_step, canvas_length * canvas_step)
    turtle.pendown()
    turtle.setpos(point1 * canvas_step, -canvas_length * canvas_step)
    turtle.penup()
    turtle.setpos(point2 * canvas_step, canvas_length * canvas_step)
    turtle.pendown()
    turtle.setpos(point2 * canvas_step, -canvas_length * canvas_step)
    turtle.penup()

canvas()

#turtle.tracer(True)

x = sympy.symbols('x')

user_input = lambda expr1, expr2: sympy.sympify(screen.textinput(expr1, expr2))

while True:
    try:
        function1 = user_input("Function 1", "Argument value:")
        graph_visualiser(function1)
        break
    except:
        turtle.title("Something gone wrong, check if you have printed everything correctly.")
        continue

is_empty = True

while True:
    try:
        function2 = user_input("Function 2", "Argument value:")
        graph_visualiser(function2)
        break
    except:
        turtle.title("Something gone wrong, check if you have printed everything correctly.")
        continue

integral_from = user_input("Define the integral:", "From:")
integral_to = user_input("Define the integral:", "To:")

intergration(integral_from, integral_to)

integral = sympy.integrate(function1-function2, (x, integral_from, integral_to))
if type(float(integral)) == type(0.0):
    print("Your integral is:")
    print(abs(float(integral)))
else:
    print(type(float(integral)))
    print("This integral is likely divergent(infinite).")

turtle.update()

turtle.mainloop()

#change2