import tkinter as tk
from tkinter import messagebox
import time
import ctypes as c
from playsound3 import playsound

user32 = c.windll.user32
d=c.windll.user32.GetDC(0)
g=c.windll.gdi32
def gdifunction():
    try:
        while True:
           time.sleep(0.1)
           g.stretchblt(d, 5, 5, 1910, 1070, d, 0, 0, 1920, 1080, 0x999999)
    except KeyboardInterrupt:
        g.DeleteDC(d)
        print("poop!")

def music():
    playsound("https://raw.githubusercontent.com/gaers-svg/ishowthneeds/main/getyopoopycomputerouttaherebro.mp3")

def open(question, answer):
    response = messagebox.askyesno(question, answer)
    if response:
        print("You chose to continue.")
        response2 = messagebox.askyesno("ishowthneeds", "this is your last chance, do you want to continue?")
        if response2:
            messagebox.showerror("ishowthneeds", "you made a huge mistake.")
            music()
            gdifunction()
        else:
            print("wise choice")
open("Warning", "This program has the full potential to destroy your computer. Do you want to continue? ")
