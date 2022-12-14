import customtkinter, getpass
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

class SettingsMain:
    def __init__(self, main):
        main.heading.set_text('SETTINGS')
