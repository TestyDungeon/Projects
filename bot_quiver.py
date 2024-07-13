import lightbulb
import hikari
# import os
# from dotenv import load_dotenv
# from discord.ext import commands



# intents = discord.Intents.default()
# intents.message_content = True

bot = lightbulb.BotApp(
    token="MTI1ODQ5OTA0MDc4NjY0NTE1Mw.G4b0cs.DqQwnn76nJtw40jiP4NWlXLQ7PWH-T6Xsw_yFc",
    default_enabled_guilds=(1258506213528834170))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot is ready')


bot.load_extensions_from("./extensions")
bot.run() 