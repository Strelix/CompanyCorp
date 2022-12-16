import getpass
import customtkinter
from Classes import TKMore as TKMore
from PIL import ImageTk, Image
from customtkinter import LEFT, RIGHT, TOP, BOTTOM
TkMore = TKMore.TKMore()

class StaffMain:
    def __init__(self, main):
        self.MAINSCREEN = main
        self.COMPANYCLASS = self.MAINSCREEN.main_screen.COMPANIES
        self.LOGINCLASS = self.MAINSCREEN.main_screen.LOGIN

        self.container = TkMore.container_main(main.container, self.MAINSCREEN)
        self.container.propagate(False)
        self.container.configure(width=main.container.winfo_width() * 0.9, height=main.container.winfo_height() * 0.8)
        self.container.pack(side=TOP, pady=(main.container.winfo_height() * 0.05, 0))
        self.MAINSCREEN.add_items_to_list(self.container)
        main.heading.set_text('STAFF')

        allowed = self.__check_company_requirements()

        if allowed:
            print('ALLOWED')

        self.MAINSCREEN.main_screen.update_idletasks()

    def __check_logged_in(self) -> bool:
        return True if self.LOGINCLASS.user_id is not None and self.LOGINCLASS.username is not None\
                       or self.LOGINCLASS.logged_in else False

    def __check_has_company(self) -> bool:
        return False if self.COMPANYCLASS.company_name is not None\
                        or self.COMPANYCLASS.company_id is not None else True

    def __check_company_requirements(self) -> bool:
        comp = self.__check_logged_in()
        login = self.__check_logged_in()
        if login and comp:
            return True

        self.MAINSCREEN.main_screen.update_idletasks()

        CONT_SIZE = self.container.winfo_height()
        CONT_SIZE = (CONT_SIZE / 2) - (CONT_SIZE * 0.05)

        self.displayText = customtkinter.CTkLabel(master=self.container, text_font='fredoka 15 bold')
        self.displayText.pack(side=TOP, pady=(CONT_SIZE, 0))
        self.MAINSCREEN.add_items_to_list(self.displayText)

        if not login:
            self.displayText.configure(text='You\'re not logged in! \n You should probably login first.')
        else:
            self.displayText.configure(text='You don\'t yet have a company. \n You can create one on '
                                            'the "COMPANY" panel.')

        return False
