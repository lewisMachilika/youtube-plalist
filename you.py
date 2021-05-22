import pytube

import pafy
from log import *
import tkinter.filedialog

#importing module 


url = input("Enter url :")
#url = "https://www.youtube.com/playlist?list=PLqM7alHXFySE71A2bQdYp37vYr0aReknt"
playlist = pytube.Playlist(url)
print(len(playlist.video_urls))

directory = tkinter.filedialog.askdirectory()

for url in playlist.video_urls:
    youtube = pytube.YouTube(url)
    print(url)
    video = youtube.streams.first()
    video.download(directory)


