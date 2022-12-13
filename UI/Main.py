import customtkinter
import Classes.TKMore
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

from UI import Login as Login
from UI import Register as Register


class Main:
    def __init__(self, main):
        self.main_screen = main
        self.items = []

        self.container = customtkinter.CTkFrame(master=main, width=main.screensize[0] - 100,
                                                height=main.screensize[1] - 120,
                                                corner_radius=20)
        self.container.pack(padx=15, pady=15)
        self.container.pack_propagate(False)

        self.heading = customtkinter.CTkLabel(master=self.container, text=' ',
                                              text_font=('FredokaOne 15 bold'))
        self.heading.pack(side=TOP, pady=15)

    def add_items_to_list(self, *items):
        try:
            for item in items:
                self.items.append(item)
        except:
            return

    def delete_item_list(self) -> None:
        return [item.destroy() for item in self.items]

    def change_page(self, page='default', *arguments):
        page = page.lower()

        self.delete_item_list()

        if page == 'default:':
            pass
        elif page == 'create_account':
            self.register = Register.RegisterMain(self)
        elif page == 'login':
            self.login = Login.LoginMain(self)
        elif page == 'staff':
            pass
        elif page == ' hack':
            pass
        elif page == '':
            pass
