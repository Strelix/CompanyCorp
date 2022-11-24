import json
from Classes.Files import Files

FILES = Files()

staff_list = FILES.read_file('staff.json')

import json
import hashlib

class Company:
    def __init__(self, database, login):
        self.staff = None
        self.DB = database
        self.login = login
        print(self.login)


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
        if self.login.logged_in and self.login.users_company_id != None:
            return False
        return True

    def create(self, name):
        print('Func: Create')
        if self.__validate_name(name):
            print(1)
            if not self.__check_exists(name):
                print(2)
                if self.__check_users_company(self.login.user_id):
                    self.DB.create_company(name, self.login.user_id)

                    companies = self.DB.get_all_companies()

                    print(f'Companies: {companies}')

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

                            return True, f'Successfully created you a company! Your starter balance is {self.balance}'

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
