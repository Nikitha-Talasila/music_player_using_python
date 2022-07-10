from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import *

mixer.init()

color1 = "#ffffff" 
color2 = "#1B1A17"


root = Tk()
root.title("MUSIC PLAYER")
root.geometry('452x335')
root.configure(background=color1)
root.resizable(width=FALSE, height=FALSE)

def show():
    
    for i in music:       
        list.insert(END, i) 

def play():
    running = list.get(ACTIVE)
    current['text'] = running
    mixer.music.load(running)
    mixer.music.play()    

def pause():
    mixer.music.pause()

def unPause():
    mixer.music.unpause()


def stop():
    mixer.music.stop()


def nextSong():
    now = current['text']
    ind=music.index(now)    
    now=music[ind+1]
    mixer.music.load(now)
    mixer.music.play()

    list.delete(0, END)

    show()
    
    list.select_set(ind+1)
    current['text']= now

def prevSong():
    now = current['text']
    ind=music.index(now)    
    now=music[ind-1]
    mixer.music.load(now)
    mixer.music.play()

    list.delete(0, END)

    show()
    
    list.select_set(ind-1)
    current['text']= now    


left = Frame(root, width=150, height=200, bg=color1)
left.grid(row=0, column=0, padx=1)

right = Frame(root, width=350, height=150, bg=color1)
right.grid(row=0, column=1, padx=0)


below = Frame(root, width=500, height=300, bg=color2)
below.grid(row=1, column=0, columnspan=3, padx=0, pady=1)


list = Listbox(right, selectmode=SINGLE, font=("Cambria 13 italic"), width=32,  bg=color2, fg=color1)
list.grid(row=0,column=0)

sb = Scrollbar(right)
sb.grid(row=0, column=1)

list.config(yscrollcommand = sb.set)
sb.config(command= list.yview)


image1 = Image.open('icons/music.png')
image1 = image1.resize((130,130))
image1 = ImageTk.PhotoImage(image1)
icon = Label(left, height=130, image=image1, padx=10, bg=color1)
icon.place(x=10, y=15)

image2 = Image.open('icons/previous.png')
image2 = image2.resize((30,30))
image2 = ImageTk.PhotoImage(image2)
prev_b = Button(below, width=40, height=40, image=image2, padx=30, bg=color1, font=("Ivy 10"),command=prevSong)
prev_b.place(x=84, y=35)

image3 = Image.open('icons/play-button.png')
image3 = image3.resize((30,30))
image3 = ImageTk.PhotoImage(image3)
play_b = Button(below, width=40, height=40, image=image3, padx=30, bg=color1, font=("Ivy 10"), command=play)
play_b.place(x=130, y=35)

image4 = Image.open('icons/next.png')
image4 = image4.resize((30,30))
image4 = ImageTk.PhotoImage(image4)
next_button = Button(below, width=40, height=40, image=image4, padx=30, bg=color1, font=("Ivy 10"), command=nextSong)
next_button.place(x=176, y=35)

image7 = Image.open('icons/continue.png')
image7 = image7.resize((30,30))
image7 = ImageTk.PhotoImage(image7)
pause_b = Button(below, width=40, height=40, image=image7, padx=30, bg=color1, font=("Ivy 10"), command=unPause)
pause_b.place(x=268, y=35)

image6 = Image.open('icons/pause.png')
image6 = image6.resize((30,30))
image6 = ImageTk.PhotoImage(image6)
continue_b = Button(below, width=40, height=40, image=image6, padx=30, bg=color1, font=("Ivy 10"), command=pause)
continue_b.place(x=222, y=35)


image5 = Image.open('icons/stop-button.png')
image5 = image5.resize((30,30))
image5 = ImageTk.PhotoImage(image5)
stop_b = Button(below, width=40, height=40, image=image5, padx=30, bg=color1, font=("Ivy 10"), command=stop)
stop_b.place(x=314, y=35)


current = Label(below, text = "Choose a Song", font=("Cambria 12 bold"), width=50, height=1, padx=10, bg=color1, fg=color2)
current.place(x=0)

os.chdir(r'C:\Users\nikit\OneDrive\Desktop\tkinter project\music')
music = os.listdir()

show()

root.mainloop()
