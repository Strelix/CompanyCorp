import customtkinter
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

class LeftBar:
    def __init__(self, ui):
        self = ui
        self.left_container = customtkinter.CTkFrame(master=self, width=100, height=self.screensize[1] - 120, corner_radius=20)
        self.left_container.pack(side=customtkinter.LEFT, padx=15, pady=15)
        self.left_container.pack_propagate(False)
        
        self.left_container_staff = customtkinter.CTkFrame(master=self.left_container, width=75, height=75, corner_radius= 20)
        self.left_container_staff.pack(side=customtkinter.TOP, padx=15, pady=15)


        staff = ImageTk.PhotoImage(file='E:\! CompanyCorp\Assets\Staff.png')
        self.left_container_staff_image = customtkinter.CTkButton(
            master=self.left_container_staff, image=staff, text='', fg_color='#292929', corner_radius=20)
        self.left_container_staff_image.pack()