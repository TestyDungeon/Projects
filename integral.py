import matplotlib.pyplot as plt
import numpy
import sympy
import sympy.integrals
import sympy.integrals.transforms

x = sympy.symbols('x')

y_ = []
x_ = []

threshold = 15

fig, ax = plt.subplots()

def argument(arg, func_type):
    return float(func_type.subs(x, arg))

func = sympy.sympify(input("X: "))

for i in numpy.linspace(-10, 10, 2000):
    try:
        y_.append(argument(i, func))
        x_.append(i) 
    except:
        continue

y_ = numpy.ma.masked_less(y_, -1*threshold) 
y_ = numpy.ma.masked_greater(y_, threshold)

ax.plot(x_, y_)

plt.grid()
plt.axis([-10, 10, -10, 10])
plt.show()