import customtkinter
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

class Main:
    def __init__(self, main):
        self.container = customtkinter.CTkFrame(master=main, width=main.screensize[0] - 100,
                                                     height=main.screensize[1] - 120,
                                                     corner_radius=20)
        self.container.pack(padx=15, pady=15)
        self.container.pack_propagate(False)

        self.heading = customtkinter.CTkLabel(master=self.container, text='BLANK',
                                                   text_font=('FredokaOne 15 bold'))
        self.heading.pack(side=TOP, pady=15)