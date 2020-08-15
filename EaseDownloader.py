from tkinter import *
from google_images_download import googleimagesdownload
from pytube import YouTube
def downloadVid():
    print("jhad")
    global E1
    string =E1.get()
    print(string)
    yt = YouTube(str(string))
    vid = yt.streams.first()
    print(vid)
    destination=str(r'C:\Users\sajma\Downloads\vid')
    vid.download(destination)
    print("\n downloaded!!")

def img():
    global E2
    global E3
    string =E2.get()
    num=E3.get()
    response = googleimagesdownload()
    absolute_image_paths = response.download({"keywords":string,"limit":num})
    print("\n downloaded!!")
    
def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
master.title("Downloader")
#master.configure(background='maroon2')

Label(master, text="GPP-EaseDownloader",font=("Helvetica", 18)).grid(row=0,column=2)

Label(master, text="Video URL",font=("Helvetica", 15)).grid(row=1,column=3)
Label(master, text="Search Images",font=("Helvetica", 15)).grid(row=1,column=0)
Label(master, text="Image Limit",font=("Helvetica", 15)).grid(row=2,column=0)

E1 = Entry(master,width="50")
E2 = Entry(master)
E3 = Entry(master)

E1.grid(row=1, column=4)
E2.grid(row=1, column=1)
E3.grid(row=2, column=1)

Button(master, text="Download video",bg="deep sky blue", command=downloadVid ).grid(row=5, column=4)
Button(master, text='Download images',bg="medium spring green", command=img).grid(row=5, column=1, sticky=W, pady=5)





