import customtkinter
from customtkinter import LEFT, RIGHT, TOP, BOTTOM
from UI import TopBar as TopBar
from UI import LeftBar as LeftBar

customtkinter.set_default_color_theme('dark-blue')
customtkinter.set_appearance_mode('dark')

class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('CompanyCorp')
        self.attributes('-fullscreen', True)

        self.screensize = self.winfo_screenwidth(), self.winfo_screenheight()

    def load_main(self):
        topbar = TopBar.TopBar(self)
        leftbar = LeftBar.LeftBar(self)


        self.main_container = customtkinter.CTkFrame(master=self, width = self.screensize[0] - 100, height=self.screensize[1] - 120,
                                                     corner_radius=20)
        self.main_container.pack(padx=15, pady=15)
        self.main_container.pack_propagate(False)

        self.main_heading = customtkinter.CTkLabel(master=self.main_container, text='BLANK', text_font=('FredokaOne 15 bold'))
        self.main_heading.pack(side =  TOP, pady = 15)





if __name__ == "__main__":
    ui = Window()

    ui.load_main()
    ui.mainloop()
