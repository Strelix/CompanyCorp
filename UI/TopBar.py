import customtkinter
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

class TopBar:
    def __init__(self, ui):
        self = ui
        self.top_bar = customtkinter.CTkFrame(master=self, width=self.screensize[0] * 0.975, height=75, corner_radius=15)
        self.top_bar.pack(side=TOP, padx=15, pady=15)
        self.top_bar.propagate(False)

        self.top_bar_quit = customtkinter.CTkButton(master=self.top_bar, text='X', width=50, height=50)
        self.top_bar_quit.pack(side=RIGHT, padx=10, pady=10)
        self.top_bar_quit.configure(fg_color='#cc1b14', text_font=('FredokaOne 15 bold'), command=quit)

        self.top_bar_minmise = customtkinter.CTkButton(master=self.top_bar, text='_', width=50, height=50)
        self.top_bar_minmise.pack(side=RIGHT, padx=10, pady=10)
        self.top_bar_minmise.configure(fg_color='#5f59ff', text_font=('FredokaOne 15 bold'), command=self.iconify)

        self.top_bar_label = customtkinter.CTkLabel(master=self.top_bar, text='CompanyCorp',
                                                           text_font=('FredokaOne 17 bold'))
        self.top_bar_label.pack(side=customtkinter.LEFT, padx=15)