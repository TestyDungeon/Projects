import hikari
import lightbulb
import requests
from bs4 import BeautifulSoup, SoupStrainer
import os
import re  
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from apiclient.discovery import build
from pytube import YouTube


# plugin = lightbulb.Plugin("Discord Music MP3 Downloader")

# def load(bot):
#     bot.add_plugin(plugin)

# @plugin.command
# @lightbulb.option("link", "Link to a song or a playlist")
# @lightbulb.command("music", "Download music")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def _integral(ctx):

api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyCn7WNc4uuVpbo-EiRtsgl_E9taCdHrAR4"

url = "https://music.youtube.com/watch?v=U-dv06NhGn8&si=vN4UVubAEfqJna3b"
r = requests.get(url)

youtube = build('youtube','v3',developerKey = api_key)

soup = BeautifulSoup(r.content, 'lxml')
content_values = [tag['content'] for tag in soup.find_all(attrs={"property" : "og:video:tag"})]
song_names = re.sub(r'[^\w]', ' ', str(content_values))
print(song_names)

request = youtube.search().list(q=song_names, part='snippet')
video_id = request.execute()["items"][0]["id"]["videoId"]
video_link = "https://www.youtube.com/watch?v=" + video_id
print(video_link)

video = YouTube(video_link)
print(video.streams)