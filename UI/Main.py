import customtkinter
import Classes.
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM


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

    def change_page(self, page='default'):
        page = page.lower()
        self.delete_item_list()
        if page == 'default:':
            pass
        elif page == 'login':
            self.heading.set_text('LOGIN')

            self.username_container = customtkinter.CTkFrame(master=self.container,
                                                             width=self.main_screen.screensize[0] * 0.3,
                                                             height=self.main_screen.screensize[1] * 0.1)

            self.username_container.pack(side=TOP, pady=(self.main_screen.screensize[1] * 0.1, 0))
            self.username_container.propagate(False)
            self.login_username_text = customtkinter.CTkLabel(master=self.username_container,
                                                              text='Username: ', text_font=('FredokaOne 13 bold'))
            self.login_username_field = customtkinter.CTkEntry(master=self.username_container)
            self.login_username_text.pack(side=LEFT)
            self.login_username_field.pack(side=RIGHT, padx=(0, 30))

            self.pin_container = customtkinter.CTkFrame(master=self.container,
                                                        width=self.main_screen.screensize[0] * 0.3,
                                                        height=self.main_screen.screensize[1] * 0.1)


            self.pin_container.propagate(False)
            self.pin_text = customtkinter.CTkLabel(master=self.pin_container,
                                                   text='PIN: ', text_font=('FredokaOne 13 bold'))
            self.pin_field = customtkinter.CTkEntry(master=self.pin_container)

            self.msg = customtkinter.CTkLabel(master=self.container, text=' ')
            self.make_account = customtkinter.CTkButton(master=self.container, text = 'Not got an account? Create 0ne!',
                                                        command = lambda: self.change_page('create_account'),
                                                        fg_color='#2B2B2B', hover_color='medium purple')

            self.login_button = customtkinter.CTkButton(master=self.container,
                                                        width=self.main_screen.screensize[0] * 0.3,
                                                        height=self.main_screen.screensize[1] * 0.06, text='LOGIN',
                                                        fg_color='purple', hover_color='medium purple',
                                                        command=lambda: self.msg.set_text(self.main_screen.LOGIN.login(
                                                            self.login_username_field.get(), self.pin_field.get())[1]))

            self.pin_container.pack(side=TOP, pady=(30, 0))
            self.pin_text.pack(side=LEFT)
            self.pin_field.pack(side=RIGHT, padx=(0, 30))
            self.login_button.pack(side=TOP, pady=(30, 0))
            self.msg.pack(side=TOP)
            self.make_account.pack(side=TOP)

            self.add_items_to_list(self.username_container, self.login_username_text, self.login_username_field,
                                   self.pin_container, self.pin_text, self.pin_field,
                                   self.msg, self.login_button, make_account)
