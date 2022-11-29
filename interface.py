import customtkinter
from customtkinter import LEFT, RIGHT, TOP, BOTTOM
from UI import TopBar as TopBar
from UI import LeftBar as LeftBar
from UI import Main as Main
from UI import Popup as Popup

customtkinter.set_default_color_theme('dark-blue')
customtkinter.set_appearance_mode('dark')


class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('CompanyCorp')
        self.attributes('-fullscreen', True)

        self.screensize = self.winfo_screenwidth(), self.winfo_screenheight()


        self.topbar = TopBar.TopBar(self)
        self.leftbar = LeftBar.LeftBar(self)
        self.main = Main.Main(self)
        self.popup = Popup.Popup(self)


    def load_main(self):


        self.topbar.text = customtkinter.CTkLabel(master=self.topbar.top_bar, text='TEST')
        self.topbar.text.pack()

        # self.topbar.


if __name__ == "__main__":
    ui = Window()

    ui.load_main()
    ui.mainloop()
