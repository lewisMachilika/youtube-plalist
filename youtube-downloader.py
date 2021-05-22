import pafy
from log import *
import tkinter.filedialog
import pytube
'''     
#tkinter.filedialog.asksaveasfilename()
#tkinter.filedialog.asksaveasfile()
#tkinter.filedialog.askopenfilename()
#tkinter.filedialog.askopenfile()
directory = tkinter.filedialog.askdirectory()
#tkinter.filedialog.askopenfilenames()
#tkinter.filedialog.askopenfiles()

url = input("Enter url :")
video = pafy.new(url)
print(video.title)

print('Rating :',video.rating,', Duration :',video.duration,', Likes :',video.likes, ', Dislikes : ', video.dislikes)
#print(video.description)

best = video.getbest()
print(best.resolution, best.extension)

best.download(quiet=False, filepath=directory+video.title+"." + best.extension)

print("saved at :",root.directory, " directory")

'''

#importing module 


url = input("Enter url :")
#url = "https://www.youtube.com/playlist?list=PLqM7alHXFySE71A2bQdYp37vYr0aReknt"

directory = tkinter.filedialog.askdirectory()


def single_url(url,directory):
    print("==================================================================================================================")
    
    video = pafy.new(url)
    print(url)
    print(video.title)

    #logs(video.title,url)
    file_object  = open(directory+"/links.log", "a")
    file_object.write(video.title +' '+ url + '\n')
    file_object.close()
    print('Rating :',video.rating,', Duration :',video.duration,', Likes :',video.likes, ', Dislikes : ', video.dislikes)
    #print(video.description)

    best = video.getbest()
    print(best.resolution, best.extension)

    best.download(quiet=False, filepath=directory+'/'+video.title+"." + best.extension)

    print("saved at :", directory, " directory")
    print("==================================================================================================================")

def playlist_func(url,directory):
    try: 
        playlist = pytube.Playlist(url)
        file_object  = open(directory+"/links.log", "a")
        file_object.write('Playlist Url :'+ url + '\n')
        file_object.close()
        print('There are {0}'.format(len(playlist.video_urls)))
        for url in playlist.video_urls:
            single_url(url,directory) 
    except:
        single_url(url,directory)
    
playlist_func(url,directory)