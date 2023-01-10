from tkinter import *
import tkinter as tk
from pytube import YouTube

root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=550, relief='raised', bg='black')
canvas1.pack()

label1= tk.Label(root, text='유튜브 다운로더맨')
label1.config(font=('helvetica',14))
canvas1.create_window(200,25,window=label1)

label2= tk.Label(root, text='주소를 입력하세용')
label1.config(font=('helvetica',14))
canvas1.create_window(200,100,window=label2)

entry1= tk.Entry(root)
canvas1.create_window(200,130,window=entry1)

def download():
    ytd_url = entry1.get()
    try:
        obj= YouTube(ytd_url)
        filter= obj.streams.filter(progressive=True,file_extension='mp4')    
        # 필터에 프로그레시브랑 설정은 머지,
        filter.get_highest_resolution().download()
        label3= tk.Label(root, text='Download is started.',font=('helvetica',10))
        canvas1.create_window(200,150,window=label3)
    except Exception as e :
        label4= tk.Label(root,text='Down failed',font=('helvetica',10))
        canvas1.create_window(200,210,window=label4)
        
button1= tk.Button(text='Download',command=download, bg='brown', fg='white', font=('helvetica',9,'bold'))
canvas1.create_window(200, 240, window=button1)
        
root.mainloop()
        