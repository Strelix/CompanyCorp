### IMPORTS ###
import json
import hashlib
from Classes.Companies import Company
## IMPORTS ##

class Login:
    def __init__(self, Database):
        self.DB = Database
        self.COMPANY = Company(self.DB, self)

        self.logged_in = False
        self.username = None
        self.user_id = None
        self.admin = False
        self.users_company_id = None


    def __check_exists(self, username)-> bool:
        taken = False
        users = self.DB.get_all_users()

        for user in users:
            if user[1] == username:
                taken = True

        return taken


    def __username_validation(self, username):
        okay = True

        for letter in username:
            if not str.isalpha(letter) and not str.isnumeric(letter):
                if letter != '_':
                    okay = False

        if len(username) < 3 or len(username) > 15:
            okay = False

        return okay

    def __get_info_by_username(self, username):
        users = list(self.DB.get_user_from_name(username))
        if len(users) != 0:
            for user in users:
                if user[1] == username:
                    return user
        return None

    def __pin_validation(self, pin):
        try:
            if len(pin) != 4:
                return False

            for digit in pin:
                if not str.isnumeric(digit):
                    return False
            return True
        except: pass

    def login(self, username, pin):
        info = self.__get_info_by_username(username)

        if info != None:
            info = list(info)
            if hashlib.sha256(pin.encode()).hexdigest() == info[2] and username == info[1]:
                self.logged_in = True
                self.username = username
                self.user_id = info[0]
                if info[3] == 1:
                    self.admin = True
                if info[4]:
                    self.users_company_id = info[4]
                self.COMPANY.set_company_info(self.users_company_id)
                return True, f'Successfully logged in!'
            else:
                return False, 'Login incorrect, please try again.'
        else:
            return False, 'Login incorrect, please try again'

    def logout(self):
        self.logged_in = False
        self.username = None
        self.user_id = None
        self.admin = False
        self.users_company_id = None
        return True, 'You\'re now logged out!'


    def signUp(self, username, pin):
        if not self.__username_validation(username):
            return False, 'This username is invalid.'
        if self.__check_exists(username):
            return False, 'This username has already been taken.'

        if not self.__pin_validation(pin):
            return False, 'Invalid pin, make sure it\'s four digits long!'

        hashed_pin = hashlib.sha256(pin.encode()).hexdigest()

        self.DB.append_user(username, hashed_pin)

        return True, f'Created user with the username of {username}! Please use !login to login with this account.'
