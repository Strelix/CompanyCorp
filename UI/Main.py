import Classes.TKMore as TKMoreClass
import customtkinter
from PIL import ImageTk, Image
from UI.MainPages import Hack as Hack
from UI.MainPages import Login as Login
from UI.MainPages import Profile as Profile
from UI.MainPages import Register as Register
from UI.MainPages import Settings as Settings
from UI.MainPages import Staff as Staff
from customtkinter import LEFT, RIGHT, TOP, BOTTOM


class Main:
    def __init__(self, main):
        self.main_screen: object = main
        self.TKMore: object = TKMoreClass.TKMore()
        self.items: list = []
        self.theme: int = 0

        self.container: object = customtkinter.CTkFrame(master=main, width=main.screensize[0] - 100,
                                                        height=main.screensize[1] - 120,
                                                        corner_radius=20)
        self.container.pack(padx=15, pady=15)
        self.container.pack_propagate(False)

        self.heading: object = customtkinter.CTkLabel(master=self.container, text=' ',
                                                      text_font=('FredokaOne', '15', 'bold'))
        self.heading.pack(side=TOP, pady=15)

    def add_items_to_list(self, *items):
        try:
            for item in items:
                self.items.append(item)
        except Exception:
            return

    def delete_item_list(self) -> None:
        return [item.destroy() for item in self.items]

    def change_page(self, page='default', *arguments):
        page: str = page.lower()

        self.delete_item_list()

        if page == 'default':
            self.heading.set_text('WELCOME!')
        if page == 'create_account':
            self.register = Register.RegisterMain(self)

        if page == 'login':
            if self.main_screen.LOGIN.logged_in:
                self.change_page('profile')
            else:
                self.login = Login.LoginMain(self)

        if page == 'profile':
            if self.main_screen.LOGIN.logged_in:
                self.profile = Profile.ProfileMain(self)

        if page == 'staff':
            self.staff = Staff.StaffMain(self)

        if page == ' hack':
            self.hack = Hack.HackMain(self)

        if page == 'settings':
            self.settings = Settings.SettingsMain(self)
