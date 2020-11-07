from pytube import Playlist,YouTube
from tkinter import filedialog
import re

from tqdm import tqdm

url=input("Paste URL here :")

#filedirectory = filedialog.askdirectory()

try:
    playlist = Playlist(url)

    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    print('Number of videos in playlist: %s' % len(playlist.video_urls))

    for url in playlist.video_urls:

        #print('Downloading from: '+ url + ", TO: " +  filedirectory)

        
        '''
        def on_progress(stream, chunk, bytes_remaining):

            total_size = stream.filesize

            bytes_downloaded = total_size - bytes_remaining 

            percentage_of_completion = bytes_downloaded / total_size * 100

            print(str(int(percentage_of_completion/1024))+"GB  " + str(percentage_of_completion/1024) + "%  " + str(int(bytes_downloaded/1024))+"GB / "+str(int(total_size/1024))+"GB", end='\r')
            
            loop = tqdm(total = int(total_size), position=0, leave=False)
            
            for k in range(int(percentage_of_completion)):

                loop.set_description("Loading...".format(k))
                
                loop.update(1)
            
            loop.close()
            
        '''
        
        yt_obj = YouTube(url)
        #yt_obj = YouTube(url, on_progress_callback=on_progress)

        #yt_obj.register_on_progress_callback(on_progress)

        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        
        # download the highest quality video

        #filters.get_highest_resolution().download()
        
        filters.get_highest_resolution().download()

        #print(url)
except Exception as e:

    print(e)

#https://www.youtube.com/watch?v=roDz8mMvbIg&list=PLknSwrodgQ72X4sKpzf5vT8kY80HKcUSe

