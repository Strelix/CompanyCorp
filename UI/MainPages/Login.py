import customtkinter, getpass
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

class LoginMain:

    def __init__(self, main):
            self.VIEW = False
            self.main_screen = main
            main.heading.set_text('LOGIN')

            self.username_container = customtkinter.CTkFrame(master=main.container,
                                                             width=main.main_screen.screensize[0] * 0.3,
                                                             height=main.main_screen.screensize[1] * 0.1)

            self.username_container.pack(side=TOP, pady=(main.main_screen.screensize[1] * 0.1, 0))
            self.username_container.propagate(False)
            self.login_username_text = customtkinter.CTkLabel(master=self.username_container,
                                                              text='Username: ', text_font=('FredokaOne 13 bold'))
            self.login_username_field = customtkinter.CTkEntry(master=self.username_container)
            self.login_username_text.pack(side=LEFT)
            self.login_username_field.pack(side=RIGHT, padx=(0, 30))

            self.pin_container = customtkinter.CTkFrame(master=main.container,
                                                        width=main.main_screen.screensize[0] * 0.3,
                                                        height=main.main_screen.screensize[1] * 0.1)


            self.pin_container.propagate(False)
            self.pin_text = customtkinter.CTkLabel(master=self.pin_container,
                                                   text='PIN: ', text_font=('FredokaOne 13 bold'))
            self.pin_field = customtkinter.CTkEntry(master=self.pin_container, show='*')
            def toggle_view():
                if self.VIEW:
                    self.pin_field.configure(show='*')
                else:
                    self.pin_field.configure(show='')
                self.VIEW = not self.VIEW

            self.show = customtkinter.CTkButton(master=self.pin_container, command=lambda: toggle_view())
            self.show.configure(width=self.pin_field.winfo_height(), text=' ', fg_color='purple', hover_color='medium purple')
            self.show.pack(side=RIGHT, padx=(0, 20))

            self.msg = customtkinter.CTkLabel(master=main.container, text=' ')
            self.make_account = customtkinter.CTkButton(master=main.container, text = 'Not got an account? Create 0ne!',
                                                        command=lambda: main.change_page('create_account'),
                                                        fg_color='#2B2B2B', hover_color='medium purple')

            self.login_button = customtkinter.CTkButton(master=main.container,
                                                        width=main.main_screen.screensize[0] * 0.3,
                                                        height=main.main_screen.screensize[1] * 0.06, text='LOGIN',
                                                        fg_color='purple', hover_color='medium purple',
                                                        command=self.login_button_press)

            self.pin_container.pack(side=TOP, pady=(30, 0))
            self.pin_text.pack(side=LEFT)
            self.pin_field.pack(side=RIGHT, padx=(0, 30))
            self.login_button.pack(side=TOP, pady=(30, 0))
            self.msg.pack(side=TOP)
            self.make_account.pack(side=TOP)

            main.add_items_to_list(self.username_container, self.login_username_text, self.login_username_field,
                                   self.pin_container, self.pin_text, self.pin_field,
                                   self.msg, self.login_button, self.make_account, self.show)

    def login_button_press(self):
        login_result = self.main_screen.main_screen.LOGIN.login(
            self.login_username_field.get(), self.pin_field.get())
        self.msg.set_text(login_result[1])

        if login_result[0]:
            self.login_button.after(200, lambda: self.main_screen.change_page('profile'))