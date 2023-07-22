from tkinter import Tk
from tkinter import *
from pytube import YouTube
from PIL import ImageTk, Image
root=Tk()
root.title("Youtube Downloader 😎")
root.geometry('570x550')
root.resizable(False,False)
root.configure(bg='#000000')
link=StringVar()
img = ImageTk.PhotoImage(Image.open("/Users/atitsharma/Desktop/photos/clipart-youtube-logo-photo-16.png"))
lovely=Label(image = img,width=570,height=550)
label_result=Label(root,width=40,height=2,text='Enter a link Below ',font=('arial',30))
link_enter = Entry(root, width=70, textvariable=link).place(x=5, y=70)
# equation=''
def OK():
    global text
    try:
        url=YouTube(str(link.get()))
        url.streams.get_highest_resolution().download()
    except:
        label_result.config(text="Error Type the correct link ")

    
Button(root,text='Download',width=10,height=10,font=('arial',30,'bold'),bd=1,fg='#FF0000',bg='#0000FF',command=lambda :OK()).place(x=5,y=180)

label_result.pack()
lovely.pack()
root.mainloop()