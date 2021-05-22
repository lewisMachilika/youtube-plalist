import pafy
from log import *
import tkinter.filedialog
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
        playlist = pafy.get_playlist(url) 
        playlist = pafy.get_playlist(url)
        print(playlist['items'][21]['pafy'])
        # getting playlist items 
        
        items = playlist["items"] 
        print('There are ',len(items), 'to be dowloaded')
        # selecting single item 
        for item in items:

            i_pafy = item['pafy'] 
                
            # getting watch url 
            y_url = i_pafy.watchv_url 
            
            # printing url 
            print(y_url)

            single_url(y_url,directory) 
    except:
        single_url(url,directory)
    
playlist_func(url,directory)