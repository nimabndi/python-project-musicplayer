import tkinter as tk

import pygame as pg

root = tk.Tk()  # make instance of tkinter
root.title('Music Player')  # title of root
root.geometry('600x400')  # select the of root
root.resizable(False, False)  # fixed the size

# Play List


# Song Track

trackFrame = tk.LabelFrame(root, text='Song Track', bg='black', fg='white', font=('Arial', 10), bd=5, relief=tk.GROOVE)
trackFrame.place(x=10, y=10, width=580, height=90)

showSongName = tk.Text(trackFrame, bg='white', fg='red', width=50, height=1, state=tk.DISABLED)
showSongName.grid(row=0, column=0, padx=10, pady=20)

showStatus = tk.Label(trackFrame, bg='white', fg='black', width=15)
showStatus.grid(row=0, column=1, padx=20)

# Control Panel
Cpanel = tk.LabelFrame(root, text='Control Panel', bg='black', fg='white', font=('Arial', 10), bd=5, relief=tk.GROOVE,
                       padx=15)
Cpanel.place(x=10, y=120, width=580, height=90)

play = tk.Button(Cpanel, text='play', width=15)
play.grid(row=0, column=0, padx=10, pady=20)

stop = tk.Button(Cpanel, text='stop', width=15)
stop.grid(row=0, column=1, padx=10, pady=20)

unpausing = tk.Button(Cpanel, text='unpausing', width=15)
unpausing.grid(row=0, column=2, padx=10, pady=20)

pausing = tk.Button(Cpanel, text='pausing', width=15)
pausing.grid(row=0, column=3, padx=10, pady=20)

root.mainloop()
