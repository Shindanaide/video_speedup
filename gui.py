#!/usr/bin/python
from tkinter import *
from tkinter import ttk, filedialog
from os import path
import sys
from moviepy import *
from moviepy.editor import *
from moviepy.editor import VideoFileClip, vfx

home = path.expanduser('~')

window = Tk()
window.title('Speedify')
window.geometry('250x200')
textEntry = Entry(window)
textEntry.insert(0,"1")
textEntry.grid(row=0, column=0, columnspan=1, rowspan=1, sticky='NW')
# Responsive
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Initialize fullscreen flag and methods
f_fullscreen = False
# Exit fullscreen
def notFullscreen(event):
    window.attributes("-fullscreen", False)
# Toggle fullscreen
def toggleFullscreen(event):
    global f_fullscreen
    f_fullscreen = not f_fullscreen
    window.attributes("-fullscreen", f_fullscreen)

# File path and getters
def getOpenFilePath():
    filepath = filedialog.askopenfilename(initialdir = home, title = "Select video",filetypes = (("MPEG-4","*.mp4"),("all files","*.*")))
    print(filepath)
    return filepath
def getSaveFilePath():
    filename = filedialog.asksaveasfilename(initialdir = home,title = "Save your new video",filetypes = (("MPEG-4","*.mp4"),
    ("all files","*.*")))
    print (filename)
    return filename
def getMultiplier():
    # Must return an Integer
    text = int(textEntry.get())
    return text

# Logic
def speedup_process():
	filename = getOpenFilePath()
	destination_filename = getSaveFilePath()
	multiplier = getMultiplier()
	
	source_video  = VideoFileClip(filename)
	newclip = source_video.speedx(factor=multiplier)
	newclip.write_videofile(destination_filename)
	return newclip
def elaborateVideo():
    newclip = speedup_process()
    newclip.write_videofile(sys.argv[2])
    return 0

# Attributes
window.attributes("-fullscreen", f_fullscreen)
# Key Bindings
window.bind("<Escape>", notFullscreen)
window.bind("<F11>", toggleFullscreen)

# Menu Window
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=window.quit)
# Buttons
openIMG = Button(window, text="GO", command=speedup_process)
openIMG.grid(row=1, column=0, columnspan=1, rowspan=1, sticky='NEWS')

# Main loop starts
window.mainloop()