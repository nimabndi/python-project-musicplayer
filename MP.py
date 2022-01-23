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

# Control Panel


root.mainloop()
