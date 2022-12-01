import customtkinter
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

class Popup:
    def __init__(self, main):
        self.main_dimensions = main.winfo_screenwidth(), main.winfo_screenheight()


        self.container = customtkinter.CTkFrame(master=main, width=self.main_dimensions[0] * 0.25,
                                                     height=self.main_dimensions[1] * 0.125,
                                                     corner_radius=0, fg_color='#333333')
        self.container.pack_propagate(False)
        # self.container.place_forget()

        self.heading = customtkinter.CTkLabel(master=self.container, text='MESSAGE',
                                                   text_font=('FredokaOne 15 bold'))
        self.heading.pack(side=TOP, pady=15)

        self.message = customtkinter.CTkLabel(master=self.container, text = ' ')
        self.message.pack(side=BOTTOM)


    def show_popup(self, message,seconds = 5, announcement_type = 'MESSAGE'):
        self.heading.set_text(announcement_type)
        self.message.set_text(message)
        self.container.place(x=(self.main_dimensions[0] * 0.05), y=(self.main_dimensions[
                                                                   1] * 0.1))  # .pack(side = LEFT, padx=15, pady=(0, main.main.container.winfo_screenheight() * 0.7))

        self.container.after((seconds * 1000), lambda: self.container.place_forget())

