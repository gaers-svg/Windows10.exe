import tkinter as tk
from tkinter import messagebox
import time
import ctypes as c
from playsound3 import playsound

user32 = c.windll.user32
d=c.windll.user32.GetDC(0)
g=c.windll.gdi32

width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

def music():
    playsound("https://raw.githubusercontent.com/gaers-svg/ishowthneeds/main/getyopoopycomputerouttaherebro.mp3")

def gdifunction():
    music()
    try:
        while True:
            g.StretchBlt(d, 0, 0, width, height, d, 0, 0, width, height, 0x00660046)
            time.sleep(0.02)
    except KeyboardInterrupt:
        print("Stopped safely")


def open(question, answer):
    response = messagebox.askyesno(question, answer)
    if response:
        print("You chose to continue.")
        response2 = messagebox.askyesno("ishowmalware", "this is your last chance, do you want to continue?")
        if response2:
            gdifunction()
            messagebox.showerror("ishowmalware", "you made a huge mistake.")
        else:
            print("wise choice")
open("Warning", "This program has the full potential to destroy your computer. Do you want to continue? ")
