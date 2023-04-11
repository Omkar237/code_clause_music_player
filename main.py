
from tkinter import *
from tkinter import  filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player Project!!")
root.geometry("920x670+290+85")
root.config(bg="#0f1a2b")
root.resizable(True, True)

mixer.init()
def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)


def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0: -4])

#icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

#logo
Logo = PhotoImage(file="logo.png")
Label(root, image=Logo).place(x=750, y=5)

#label
music = Label(root, text="", font=("arial",15))
music.place(x=190, y=140, anchor="center")
#button
play_button = PhotoImage(file="play.png")
Button(root, image=play_button, command=play_song).place(x=100, y=500)

Stop_button = PhotoImage(file="stop.png")
Button(root, image=Stop_button, command=mixer.music.stop).place(x=320, y=500)

resume_button = PhotoImage(file="resume.png")
Button(root, image=resume_button, command=mixer.music.unpause).place(x=700, y=500)

pause_button = PhotoImage(file="pause.png")
Button(root, image=pause_button, command=mixer.music.pause).place(x=520, y=500)

#music

Menu=PhotoImage(file="menu.png")
Label(root, image=Menu).pack(padx=10,pady=50, side=LEFT)

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.pack(padx=10, pady=50, side=LEFT)

Button(root, text="Open Folder", width=15, height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de", command=open_folder).place(x=200, y=300)
scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame, width=100, font=("arial",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=LEFT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)



root.mainloop()