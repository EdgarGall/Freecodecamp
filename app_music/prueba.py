from tkinter import *
from PIL import Image, ImageTk
import pygame

root = Tk()
root.title("Usando Pygame")
root.iconbitmap("img\imagenes\icon\iconousar.ico")
root.geometry("800x800")

def eladio():
    pygame.mixer.init()
    pygame.mixer_music.load("app_music\music\y2mate.com - Eladio Carrión  Mbappe Video Oficial  SEN2 KBRN VOL 2.mp3")
    pygame.mixer.music.play()
    return

def bad():
    pygame.mixer.init()
    pygame.mixer_music.load("app_music\music\y2mate.com - BAD BUNNY  MONACO Official Video  nadie sabe lo que va a pasar mañana.mp3")
    pygame.mixer.music.play()
    return








root.mainloop()
