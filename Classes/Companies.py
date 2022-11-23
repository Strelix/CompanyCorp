import json
from Classes.Files import Files

FILES = Files()

staff_list = FILES.read_file('staff.json')

import json
import hashlib


class Login:
    def __init__(self, Database):
        self.DB = Database

        self.logged_in = False
        self.username = None
        self.user_id = None
        self.admin = False
        self.users_company_id = None

    def __check_exists(self, username) -> bool:
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
        users = self.DB.get_all_users()

        for user in users:
            if user[1] == username:
                return user

    def __pin_validation(self, pin):
        try:
            if len(pin) != 4:
                return False

            for digit in pin:
                if not str.isnumeric(digit):
                    return False
            return True
        except:
            pass

    def login(self, username, pin):
        info = self.__get_info_by_username(username)

        if hashlib.sha256(pin.encode()).hexdigest() == info[2]:
            self.logged_in = True
            self.username = username
            self.user_id = info[0]



            if info[3] == 1:
                self.admin = True
            if info[4]:
                self.users_company_id = info[4]

            return True, f'Successfully logged in!'
        else:
            return False, 'Login incorrect, please try again.'

    def logout(self):
        self.logged_in = False
        self.username = None
        self.user_id = None
        self.admin = False
        self.users_company_id = None
        print('You\'re now logged out!')

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


class Company:
    def __init__(self, database):
        self.staff = None
        self.DB = database

        self.LOGIN = Login(self.DB)

        help(self.LOGIN)

        self.company_name = None
        self.balance = None
        self.company_id = None
        # self.staff = {"hr": 0, "hacker": 0, "spy": 0}


    def save(self):
        self.DB.save_company(self.company_id, self.balance, self.staff, self.login.user_id)

    def __validate_name(self, name):
        for letter in name:
            if not str.isnumeric(letter) and not str.isalpha(letter):
                return False

        if 4 <= len(name) < 15:
            return True

        return False

    def __check_exists(self, name) -> bool:
        taken = False
        companies = self.DB.get_all_companies()

        if not companies:
            return

        for user in companies:
            if user[1] == name:
                taken = True

        return taken

    def __check_users_company(self, owner):
        if self.login.logged_in and self.login.users_company_id:
            return False
        return True

    def create(self, name):
        if self.__validate_name(name) and not self.__check_exists(name) and not self.__check_users_company(self.login.user_id):
            self.DB.create_company(name, self.login.user_id)

            companies = self.DB.get_all_companies()

            for company in companies:
                if company[4] == self.login.user_id:

                    self.login.users_company_id = company[0] # sets id
                    self.company_name = company[1]
                    self.balance = company[2]
                    self.company_id = company[0]
                    self.staff = company[3]

                    # for member in company[3]:
                    #

                    self.DB.add_company_to_user(self.company_id, self.login.user_id)

    def set_company_info(self, comp_id):
        data = self.DB.get_all_companies()
        for item in data:
            if item[0] == comp_id:
                self.company_name = item[1]
                self.balance = item[2]
                self.company_id = item[0]
                self.staff = json.loads(item[3])[0]
                print(f'Staff: {self.staff}')

        self.company_id = comp_id

    def get_company(self):
        if not self.__check_users_company(self.login.user_id):
            for company in self.DB.get_all_companies():
                if company[4] == self.login.user_id:
                    return company
        return False


    def add_money(self, amount):
        self.balance += amount
        self.DB.add_company_money(self.login.users_company_id, amount)

    def remove_money(self, amount):
        self.balance -= amount
        self.DB.remove_company_money(self.login.users_company_id, amount)

    def get_balance(self):
        return self.DB.get_company_balance(self.login.users_company_id)

    def get_staff(self):
        return self.staff

    def hire_staff(self, type):
        if type in staff_list[0]:
            item = staff_list[0][type]
            price = item['price']
            max = item['max']

            if self.staff[type] < max:
                self.staff[type] += 1
                self.remove_money(price)

                self.save()
                return self.staff

        return False
