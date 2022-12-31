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
        self.POPUP = self.MAINSCREEN.main_screen.popup

        self.container = TkMore.container_main(main.container, self.MAINSCREEN)
        self.container.propagate(False)
        self.container.configure(width=main.container.winfo_width() * 0.9, height=main.container.winfo_height() * 0.8)
        self.container.pack(side=TOP, pady=(main.container.winfo_height() * 0.05, 0))
        self.MAINSCREEN.add_items_to_list(self.container)
        main.heading.set_text('STAFF')

        allowed = self.__check_company_requirements()

        if allowed:
            LOAD_STAFF = self.__load_staff()

            self.hire_staff = TkMore.button_purple(self.container, 'HIRE STAFF')
            self.hire_staff.configure(command=self.__hire_staff)
            self.hire_staff.pack()
            self.MAINSCREEN.add_items_to_list(self.hire_staff)

            if LOAD_STAFF:
                pass

        self.MAINSCREEN.main_screen.update_idletasks()

    def __check_logged_in(self) -> bool:
        return True if self.LOGINCLASS.user_id is not None and self.LOGINCLASS.username is not None \
                       or self.LOGINCLASS.logged_in else False

    def __check_has_company(self) -> bool:
        return False if self.COMPANYCLASS.company_name is not None \
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

    def __load_staff(self):
        pass

    def __hire_staff(self):
        all_staff = self.MAINSCREEN.main_screen.FILES.read_file('staff.json')[0]
        options = []
        [options.append(x.capitalize() if x != 'hr' else 'HR') for x in all_staff]
        self.select_staff_hire = customtkinter.CTkOptionMenu(self.container, values=options)
        self.select_staff_hire.set('Select')
        self.MAINSCREEN.add_items_to_list(self.select_staff_hire)
        self.select_staff_hire.pack()

        self.hire_staff_hire_btn = TkMore.button_purple(self.container, 'HIRE STAFF MEMBER')
        self.hire_staff_hire_btn.pack()

        self.hire_staff_hire_btn.configure(command=self.__buy_staff)


        self.main_screen.add_items_to

    def __buy_staff(self):
        staff_to_hire_main = self.select_staff_hire.get()
        staff_to_hire = staff_to_hire_main.lower()
        return_message = self.COMPANYCLASS.hire_staff(staff_to_hire)
        amount = self.COMPANYCLASS.get_staff()[staff_to_hire]

        if return_message[0] == True:
            self.POPUP.show_popup(f'{return_message[1]} \n You now have {amount} {staff_to_hire_main} staff members.',
                                  3, 'SUCCESS', 'green')
        else:
            print(f'Return msg {return_message[0]}')
            self.POPUP.show_popup(f'{return_message[1]}', 5, 'ERROR', 'red')
