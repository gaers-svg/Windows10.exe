from sys import exception
import tkinter as tk
from tkinter import messagebox
import time
import ctypes as c
import subprocess
import threading
from playsound3 import playsound

def play_sound():
    playsound("https://github.com/gaers-svg/ishowthneeds/raw/refs/heads/main/bytebeat1.mp3")


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
    
import win32gui
import win32api
import win32ui
import win32con

def gdifunction2():
    try:
        while True:
            hdesktop = win32gui.GetDesktopWindow()
            hdc_screen = win32gui.GetDC(hdesktop)
            hdc_mem = win32ui.CreateDCFromHandle(hdc_screen).CreateCompatibleDC()
            width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
            height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
            win32gui.StretchBlt(
                hdc_screen, 0, 0, width, height, 
                hdc_mem.GetHandle_(), 0, 0, width // 2, height // 2, 
                win32con.SRCCOPY
            )
            time.sleep(0.1)
    except exception as e  :
        print("poopy computer")

def open(question, answer):
    response = messagebox.askyesno(question, answer)
    if response:
        print("You chose to continue.")
        response2 = messagebox.askyesno("Last Warning", "This program will destroy your computer if you say yes. Do you want to continue?")
        if response2:
            messagebox.showerror("ishowthneeds", "you made a huge mistake.")
            threading.Thread(target=play_sound, daemon=True).start()
            gdifunction()
            gdifunction2()
        else:
            print("wise choice")
open("Warning", "This program has the full potential to destroy your computer. Do you want to continue? ")
