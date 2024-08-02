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
import yt_dlp
import ffmpeg


plugin = lightbulb.Plugin("Discord Music MP3 Downloader")

def load(bot):
    bot.add_plugin(plugin)

@plugin.command
@lightbulb.option("link", "Link to a song")
@lightbulb.command("music", "Download a song from Spotify or Youtube")
@lightbulb.implements(lightbulb.SlashCommand)
async def _integral(ctx):
    await ctx.respond("Looking for your song...")

    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyCn7WNc4uuVpbo-EiRtsgl_E9taCdHrAR4"

    url = ctx.options.link
    r = requests.get(url)

    youtube = build('youtube','v3',developerKey = api_key)

    soup = BeautifulSoup(r.content, 'lxml')

    if url[8] == "o":
        title = soup.find('title').get_text()
        song_names, author_part = title.split(" - song by ")
        author_name = author_part.split(" | ")[0]
        song_names += " " + author_name
    elif url[8] == "m":
        content_values = [tag['content'] for tag in soup.find_all(attrs={"property" : "og:video:tag"})]
        if len(content_values) > 8:
            print(soup.find_all("title")[1])
            #print(content_values)
            song_names = soup.find_all("title")[1].text
        else:
            song_names = re.sub(r'[^\w]', ' ', str(content_values)) + soup.find_all("title")[1].text

    song_names = song_names.replace("Music", "").replace("YouTube", "")
    #print("Content values: ", content_values)
    print("Song names: ", song_names)
    #print(soup.prettify())
    # with open("file1.txt", "w") as file:
    #     file.write(soup.prettify())


    # Split the title to get the song name and author

    request = youtube.search().list(q=song_names, part='snippet')
    # with open("request1.txt", "w") as file:
    #     file.write(str(request.execute()))
    video_id = request.execute()["items"][0]["id"]["videoId"]
    video_link = "https://www.youtube.com/watch?v=" + video_id
    print("Link: ", video_link)

    file_name = song_names.replace(" ", "")

    ydlp_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        #"paths" : {"home" : "extensions/songs"},
        'outtmpl' : file_name + '.%(ext)s'
    }

    await ctx.edit_last_response("Downloading...")

    with yt_dlp.YoutubeDL(ydlp_opts) as ydlp:
       ydlp.download([video_link])

    file = hikari.File(file_name + ".mp3")

    await ctx.edit_last_response(file)
    await ctx.edit_last_response(file_name)
    os.remove(file_name + ".mp3")