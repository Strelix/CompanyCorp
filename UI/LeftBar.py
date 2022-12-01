import customtkinter
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM


class LeftBar:
    def __init__(self, main):
        self.container = customtkinter.CTkFrame(master=main, width=100, height=main.screensize[1] - 120,
                                                     corner_radius=20)
        self.container.pack(side=LEFT, padx=15, pady=15)
        self.container.pack_propagate(False)

        self.staff = customtkinter.CTkButton(master=self.container, hover_color='#333333',  fg_color='#222222', width=75, height=75, corner_radius=20)
        self.staff.pack(side=TOP, padx=15, pady=15)
        self.staff.propagate(False)

        staff = ImageTk.PhotoImage(file='./Assets/Staff.png')
        login = None

        self.staff_image = customtkinter.CTkButton(
            master=self.staff, image=staff, text='',  fg_color='#222222', corner_radius=20)
        self.staff_image.pack(padx=5, pady=15)

        # self.staff_image.bind("<Enter>", lambda b:  self.staff_image.configure(background='green'))
        # self.staff_image.bind("<Leave>", lambda b: self.staff_image.configure(background='red'))

        self.settings = customtkinter.CTkButton(master=self.container, text='', hover_color='#333333', fg_color='#222222',  width=75, height=75, corner_radius=20)
        self.settings.pack(side=BOTTOM, padx=15, pady=15)

        self.login = customtkinter.CTkButton(master=self.container,
                                             text='', fg_color='#222222',
                                             hover_color='#333333',  width=75,
                                             height=75, corner_radius=20,
                                             command=lambda: main.main.change_page('LOGIN'))
        self.login.pack(side=BOTTOM, padx=15, pady=15)




