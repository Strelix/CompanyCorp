import customtkinter
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

class Popup:
    def __init__(self, main):
        self.container = customtkinter.CTkFrame(master=main.main.container, width=main.main.container.winfo_screenwidth() * 0.25,
                                                     height=main.main.container.winfo_screenheight() * 0.125,
                                                     corner_radius=20, background='green')
        self.container.pack(side = LEFT, padx=15, pady=(0, main.main.container.winfo_screenheight() * 0.7))
        self.container.pack_propagate(False)

        self.heading = customtkinter.CTkLabel(master=self.container, text='POPUP MESSAGE',
                                                   text_font=('FredokaOne 15 bold'))
        self.heading.pack(side=TOP, pady=15)