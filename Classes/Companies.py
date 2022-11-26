### IMPORTS ###
import json, hashlib
from Classes.Files import Files
## IMPORTS ##
### INITIALISE VARIABLES ###
FILES = Files()
staff_list = FILES.read_file('staff.json')
## INITIALISE VARIABLES ##

class Company:
    def __init__(self, database, login):
        self.staff = None
        self.DB = database
        self.login = login
        self.company_name = None
        self.balance = None
        self.company_id = None
        # self.staff =
        # {"hr": 0, "hacker": 0, "spy": 0}
        # instead of: [0,0,0]

    # Save a users data
    def save(self):
        self.DB.save_company(self.company_id, self.balance, self.staff, self.login.user_id)

    # Check if a name of a company is valid
    def __validate_name(self, name) -> bool:
        for letter in name:
            # IF IT IS A SYMBOL, RETURN FALSE (NOT VALID)
            if not str.isnumeric(letter) and not str.isalpha(letter):
                return False

        if 4 <= len(name) < 15:
            return True

        return False

    # Check if a company exists with that name
    def __check_exists(self, name) -> bool:
        taken = False
        companies = self.DB.get_all_companies()

        if not companies:
            return False

        for company in companies:
            if company[1] == name:
                taken = True
        return taken

    # Check if a user already owns a company
    def __check_users_company(self, owner) -> bool:
        if self.login.users_company_id != None:
            return True
        return False



    # CREATES A COMPANY
    def create(self, name):
        if self.__validate_name(name) and \
            not self.__check_exists(name) and \
            not self.__check_users_company(self.login.user_id):
                    self.DB.create_company(name, self.login.user_id)
                    companies = self.DB.get_all_companies()
                    for company in companies:
                        if company[4] == self.login.user_id:
                            # sets the values (like it would do if you logged in and had a companya
                            self.login.users_company_id = company[0] # sets id
                            self.company_name = company[1]
                            self.balance = company[2]
                            self.company_id = company[0]
                            self.staff = company[3]

                            # ADDS the company id to the users database "company_id"
                            self.DB.add_company_to_user(self.company_id, self.login.user_id)

                            return True, f'Successfully created you a company! Your starter balance is {self.balance}'
        else:
            return False, 'Either your comapny name is invalid or the name is taken! Make sure it doesn\'t contain symbols.'

    def set_company_info(self, comp_id):
        data = list(self.DB.get_company_from_id(comp_id)[0])
        if data:
            self.company_id = data[0]
            self.company_name = data[1]
            self.balance = data[2]
            self.staff = dict(json.loads(data[3]))
            self.owner_id = data[4]
        return data

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
            if self.balance >= price:
                if float(self.staff[type]) < float(max):
                    self.staff[type] += 1
                    self.remove_money(price)

                    self.save()
                    return self.staff
                else:
                    return False, 'You have the maximum number of this staff type!'
            else:
                return False, 'You don\' have enough money to do this!'



        return False


    def delete_company(self):
        self.DB.delete_company(self.company_id, self.login.user_id)

    def get_company_info(self):
        return {"id": self.company_id, "name": self.company_name, "balance": self.balance, "staff": self.staff}
