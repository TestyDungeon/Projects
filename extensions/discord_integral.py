import hikari
import lightbulb
import matplotlib.pyplot as plt
import numpy
import sympy
import sympy.integrals
import sympy.integrals.transforms
import os
import traceback

plugin = lightbulb.Plugin("Discord Integral")

def load(bot):
    bot.add_plugin(plugin)

@plugin.command
@lightbulb.option("point_to", "Enter the finish integration point")
@lightbulb.option("point_from", "Enter the start integration point")
@lightbulb.option("func2", "Enter the argument of the second function")
@lightbulb.option("func1", "Enter the argument of the first function")
@lightbulb.command("integral", "Find an integral of two functions")
@lightbulb.implements(lightbulb.SlashCommand)
async def _integral(ctx):
    await ctx.respond("Generating your graph...")

    user_input_arguments = (ctx.options.func1, ctx.options.func2)
    user_input_integral = (ctx.options.point_from, ctx.options.point_to)
    

    y_ = []
    x_ = []

    threshold = 15

    fig, ax = plt.subplots()
    plt.grid()
    plt.axis([-10, 10, -10, 10])

    x = sympy.symbols('x')

    def argument(arg, func_type):
        return float(func_type.subs(x, arg))
    
    for inp in user_input_arguments:
        print(inp)
        func = sympy.sympify(inp)
        print("pre for")

        for i in numpy.linspace(-10, 10, 2000):
            try:
                y_.append(argument(i, func))
                x_.append(i) 
            except:
                continue

        print(y_[::5])

        y_ = numpy.ma.masked_less(y_, -1*threshold) 
        y_ = numpy.ma.masked_greater(y_, threshold)
        print(y_[::5])
        ax.plot(x_, y_)
        x_ = []
        y_ = []
    
    result = abs((sympy.integrate(sympy.sympify(user_input_arguments[0])-sympy.sympify(user_input_arguments[1]), (x, user_input_integral[0], user_input_integral[1]))))

    plt.savefig("image")

    await ctx.edit_last_response(hikari.File("image.png"))
    await ctx.edit_last_response("Integral = " + str(result))
    os.remove("image.png")