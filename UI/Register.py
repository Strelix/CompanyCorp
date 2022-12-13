import customtkinter
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

class RegisterMain:
    def __init__(self, main):
            main.heading.set_text('REGISTER')

            self.username_container = customtkinter.CTkFrame(master=main.container,
                                                             width=main.main_screen.screensize[0] * 0.3,
                                                             height=main.main_screen.screensize[1] * 0.1)

            self.username_container.pack(side=TOP, pady=(main.main_screen.screensize[1] * 0.1, 0))
            self.username_container.propagate(False)
            self.register_username_text = customtkinter.CTkLabel(master=self.username_container,
                                                              text='Username: ', text_font=('FredokaOne 13 bold'))
            self.register_username_field = customtkinter.CTkEntry(master=self.username_container)
            self.register_username_text.pack(side=LEFT)
            self.register_username_field.pack(side=RIGHT, padx=(0, 30))

            self.pin_container = customtkinter.CTkFrame(master=main.container,
                                                        width=main.main_screen.screensize[0] * 0.3,
                                                        height=main.main_screen.screensize[1] * 0.1)


            self.pin_container.propagate(False)
            self.pin_text = customtkinter.CTkLabel(master=self.pin_container,
                                                   text='PIN: ', text_font=('FredokaOne 13 bold'))
            self.pin_field = customtkinter.CTkEntry(master=self.pin_container, show='*')

            self.msg = customtkinter.CTkLabel(master=main.container, text=' ')
            self.login_to_account = customtkinter.CTkButton(master=main.container, text = 'Already have an account? LOGIN!',
                                                        command=lambda: main.change_page('login'),
                                                        fg_color='#2B2B2B', hover_color='medium purple')

            self.register_button = customtkinter.CTkButton(master=main.container,
                                                        width=main.main_screen.screensize[0] * 0.3,
                                                        height=main.main_screen.screensize[1] * 0.06, text='REGISTER',
                                                        fg_color='purple', hover_color='medium purple',
                                                        command=lambda: self.msg.set_text(main.main_screen.LOGIN.sign_up(
                                                            self.register_username_field.get(), self.pin_field.get())[1]))

            self.pin_container.pack(side=TOP, pady=(30, 0))
            self.pin_text.pack(side=LEFT)
            self.pin_field.pack(side=RIGHT, padx=(0, 30))
            self.register_button.pack(side=TOP, pady=(30, 0))
            self.msg.pack(side=TOP)
            self.login_to_account.pack(side=TOP)

            main.add_items_to_list(self.username_container, self.register_username_text, self.register_username_field,
                                   self.pin_container, self.pin_text, self.pin_field,
                                   self.msg, self.register_button, self.login_to_account)