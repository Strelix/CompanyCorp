import customtkinter, getpass
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM

from Classes import TKMore

from Classes import TKMore as TKMore

TkMore = TKMore.TKMore()


class ProfileMain:
    def __init__(self, main):
            self.main_screen = main
            main.heading.set_text('Your Profile')
            self.container = TkMore.container_main(main.container, main)
            self.container.propagate(False)
            self.container.pack(side=TOP, pady=(main.main_screen.screensize[1] * 0.1, 0))
            self.logout = main.TKMore.button_purple(self.container, 'Logout of your account')
            self.logout.configure(command = lambda: self.F_logout())
            self.logout.pack()

            self.main_screen.add_items_to_list(self.logout, self.container)

    def F_logout(self):
            self.main_screen.main_screen.LOGIN.logout()
            self.main_screen.change_page('default')