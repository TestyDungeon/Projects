import hikari
import lightbulb
import requests
from bs4 import BeautifulSoup, SoupStrainer
import os
import re  
import urllib.request

# plugin = lightbulb.Plugin("Discord Music MP3 Downloader")

# def load(bot):
#     bot.add_plugin(plugin)

# @plugin.command
# @lightbulb.option("link", "Link to a song or a playlist")
# @lightbulb.command("music", "Download music")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def _integral(ctx):

url = "https://music.youtube.com/watch?v=dGzvyW4_T5U&si=uVTCLSeYn9-iHhvR"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
content_values = [tag['content'] for tag in soup.find_all(attrs={"property" : "og:video:tag"})]
song_names = re.sub(r'[^\w]', '+', str(content_values))
print(song_names)

html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + song_names)
print(html.read().decode())

# soup2 = BeautifulSoup(r2.content, 'html.parser', parse_only=SoupStrainer('a'))

# for link in soup2:
#     if link.has_attr('href'):
#         print(link['href'])