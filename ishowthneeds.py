import io
import tkinter as tk
from tkinter import messagebox
import time
import subprocess
import pygame
import winsound
import urllib.request

def gdifunction():
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
        response2 = messagebox.askyesno("ishowmalware", "this is your last chance, do you want to continue?")
        if response2:
            messagebox.showerror("ishowmalware", "you made a huge mistake.")
            gdifunction()
        else:
            print("wise choice")
open("Warning", "This program has the full potential to destroy your computer. Do you want to continue? ")
