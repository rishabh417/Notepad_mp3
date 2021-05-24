from tkinter import *
from tkinter.messagebox import showinfo
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
root = Tk()
root.title("R_N_cum_M")
root.wm_iconbitmap("8.ico")
root.geometry("456x655")
import pygame
pygame.mixer.init()

def playmusic():
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stopmusic():
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.stop()

   
def addmusic():
    adding = askopenfilename(defaultextension=".mp3", filetypes=[("All File", "*.*"), ("Audio", "*.mp3")])
    song_box.insert(END,adding)

def removemusic():
    song_box.delete(ACTIVE)

def fusemp3():
    frame.pack(side=RIGHT, fill=Y)
    frame1.pack(side=TOP, fill=X)
    pass
def defusemp3():
    frame.pack_forget()
    frame1.pack_forget()

frame = Frame(root)
# frame.pack(side=RIGHT, fill=Y)
# label = Label(frame,text="Music")
# label.pack()
frame1 = Frame(root, bg="indigo")
# frame1.pack(side=TOP, fill=X)
# label1 = Label(frame1,text="List box")
# label1.pack()
control_button_play_image = PhotoImage(file="play.png")
control_button_stop_image = PhotoImage(file="stop.png")

control_button_play_button = Button(
    frame, image=control_button_play_image, command=playmusic)
control_button_play_button.pack()
control_button_stop_button = Button(
    frame, image=control_button_stop_image, command=stopmusic)
control_button_stop_button.pack()
add_music_button = Button(frame, text="Add \n  Music",
                          font="helvetica 12 bold underline",command=addmusic)
add_music_button.pack()
remove_music_button = Button(frame, text="Remove \n  Music",
                          font="helvetica 12 bold underline",command=removemusic)
remove_music_button.pack()


def newfile():
    global file
    file = None
    textArea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All File", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"-R_N_cum_M")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()


def saveas():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[
                                 ("All File", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+"-R_N_cum_M")
    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()


def cut():
    textArea.event_generate(("<<Cut>>"))


def copy():
    textArea.event_generate(("<<Copy>>"))


def paste():
    textArea.event_generate(("<<Paste>>"))


def requestacall():
    showinfo("Your Request is Accepted", "Our team will reach you soon")
def credit():
    showinfo("Owner name : ","Rishabh Singh of Prayagraj,Uttar Pradesh,India is maker of this application")

def rateus():
    text = tmsg.askquestion("Feedback", "Was your experience good")
    if text == "yes":
        msg = "Thanks for using our service"
    else:
        msg = "Sorry for the inconvenience"
    showinfo("Thanks for giving the feedback", msg)


song_box = Listbox(frame1, bg="black", fg="green")
song_box.pack(fill=X)

textArea = Text(root)
file = None
textArea.pack(expand=True, fill=BOTH)
notepadMenu = Menu()
nm1 = Menu(notepadMenu, tearoff=0)
nm1.add_command(label="New File", command=newfile)
nm1.add_command(label="Open File", command=openfile)
nm1.add_command(label="Save As", command=saveas)
nm1.add_command(label="Exit", command=root.destroy)
notepadMenu.add_cascade(label="File", menu=nm1)
root.config(menu=notepadMenu)
nm2 = Menu(notepadMenu, tearoff=0)
nm2.add_command(label="Cut", command=cut)
nm2.add_command(label="Copy", command=copy)
nm2.add_command(label="Paste", command=paste)
notepadMenu.add_cascade(label="Edit", menu=nm2)
root.config(menu=notepadMenu)
nm3 = Menu(notepadMenu, tearoff=0)
nm3.add_command(label="Request a call", command=requestacall)
notepadMenu.add_cascade(label="Help", menu=nm3)
root.config(menu=notepadMenu)
notepadMenu.add_cascade(label="Rate us", command=rateus)
notepadMenu.add_cascade(label="Fuse_MP3", command=fusemp3)
notepadMenu.add_cascade(label="Defuse_MP3", command=defusemp3)
notepadMenu.add_cascade(label="Credit", command=credit)
root.mainloop()
