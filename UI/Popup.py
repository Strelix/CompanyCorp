import customtkinter
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

class Popup:
    def __init__(self, main):
        main_dimensions = main.winfo_screenwidth(), main.winfo_screenheight()


        self.container = customtkinter.CTkFrame(master=main, width=main_dimensions[0] * 0.25,
                                                     height=main_dimensions[1] * 0.125,
                                                     corner_radius=0, fg_color='#333333')
        self.container.place(x=(main_dimensions[0] * 0.05), y=(main_dimensions[1] * 0.1)) # .pack(side = LEFT, padx=15, pady=(0, main.main.container.winfo_screenheight() * 0.7))
        self.container.pack_propagate(False)

        self.heading = customtkinter.CTkLabel(master=self.container, text='POPUP MESSAGE',
                                                   text_font=('FredokaOne 15 bold'))
        self.heading.pack(side=TOP, pady=15)