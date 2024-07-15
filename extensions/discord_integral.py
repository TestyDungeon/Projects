import hikari
import lightbulb
import matplotlib.pyplot as plt
import numpy
import sympy
import sympy.integrals
import sympy.integrals.transforms
import os

plugin = lightbulb.Plugin("Discord Integral")

def load(bot):
    bot.add_plugin(plugin)

@plugin.command
#@lightbulb.option("func2", "Enter the argument of the second function")
@lightbulb.option("func1", "Enter the argument of the first function")
@lightbulb.command("integral", "Find an integral of two functions")
@lightbulb.implements(lightbulb.SlashCommand)
async def _integral(ctx):
    user_input = ctx.options.func1
    #user_input_2 = ctx.options.func2  

    threshold = 15

    fig, ax = plt.subplots()

    y_ = []
    x_ = []

    x = sympy.symbols('x')

    def argument(arg, func_type):
        print(float(func_type.subs(x, arg)))
        return float(func_type.subs(x, arg))

    func = sympy.sympify(user_input)

    for i in numpy.linspace(-10, 10, 2000):
        try:
            y_.append(argument(i, func))
            x_.append(i) 
        except:
            continue

    y_ = numpy.ma.masked_less(y_, -1*threshold) 
    y_ = numpy.ma.masked_greater(y_, threshold)
    print("pre plot")
    ax.plot(x_, y_)
    print("post plot")
    plt.grid()
    plt.axis([-10, 10, -10, 10])
    plt.savefig("image")
    print("post save")

    await ctx.respond(hikari.File("image.png"))
    print("post respond")
    os.remove("image.png")