import tkinter as tk
from tkinter import messagebox
import time
import ctypes as c
from playsound3 import playsound
import pygame
import subprocess

user32 = c.windll.user32
d=c.windll.user32.GetDC(0)
g=c.windll.gdi32

width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

def music():
    playsound("https://raw.githubusercontent.com/gaers-svg/ishowthneeds/main/getyopoopycomputerouttaherebro.mp3")

def gdifunction():
    try:
        while True:
            # 0x00330008 = NOTSRCCOPY → invert the screen
            g.StretchBlt(d, 0, 0, width, height, d, 0, 0, width, height, 0x00330008)
            time.sleep(0.02)
    except KeyboardInterrupt:
        print("Stopped safely")
def gdifunction2():
    try:
        while True: 
            subprocess.run(["python", "-c", "import ctypes as c; g=c.windll.gdi32;d=c.windll.user32.GetDC(0);[g.StretchBlt(d, 5, 5, 1910, 1070, d, 0, 0, 1920, 1080, 0x999999) for _ in range(10**1)]"])
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

    except Exception as e:
        print(f"An error occurred: {e}")

def open(question, answer):
    response = messagebox.askyesno(question, answer)
    if response:
        print("You chose to continue.")
        response2 = messagebox.askyesno("ishowthneeds", "this is your last chance, do you want to continue?")
        if response2:
            messagebox.showerror("ishowthneeds", "you made a huge mistake.")
            gdifunction()
            gdifunction2()
            music()
        else:
            print("wise choice")
open("Warning", "This program has the full potential to destroy your computer. Do you want to continue? ")
