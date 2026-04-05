from sys import exception
import tkinter as tk
from tkinter import messagebox
import time
import ctypes as c
import subprocess
import threading
from playsound3 import playsound

def play_sound():
    playsound("https://github.com/gaers-svg/ishowthneeds/raw/refs/heads/main/getyopoopycomputerouttaherebro.mp3")


user32 = c.windll.user32
d=c.windll.user32.GetDC(0)
g=c.windll.gdi32

width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

def gdifunction():
    
    try:
        while True: 
            g.StretchBlt(d, 5, 5, width, height, d, 0, 0, 1920, 1080, 0x00990066)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("67")
    
def gdifunction2():
    try:
        while True: 
            subprocess.run(["python", "-c", "import ctypes as c; g=c.windll.gdi32;d=c.windll.user32.GetDC(0);[g.StretchBlt(d, 5, 5, " + str(width) + ", " + str(height) + ", d, 0, 0, 1920, 1080, 0x999999) for _ in range(10**1)]"])
            time.sleep(0.5)

    except exception:
        print(f"poopy computer outtaherebro")

def open(question, answer):
    response = messagebox.askyesno(question, answer)
    if response:
        print("You chose to continue.")
        response2 = messagebox.askyesno("Last Warning", "This program will destroy your computer if you say yes. Do you want to continue?")
        if response2:
            messagebox.showerror("ishowthneeds", "you made a huge mistake.")
            threading.Thread(target=play_sound, daemon=True).start()
            gdifunction()
        else:
            print("wise choice")
open("Warning", "This program has the full potential to destroy your computer. Do you want to continue? ")
