import lightbulb
import hikari
import os

bot = lightbulb.BotApp(
    token="",
    default_enabled_guilds=(1258506213528834170))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot is ready')


bot.load_extensions_from("./extensions")
bot.run() 
