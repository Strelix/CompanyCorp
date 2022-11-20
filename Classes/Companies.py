class Company:
    def __init__(self, database, login):
        self.DB = database

        self.login = login

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
                    self.DB.add_company_to_user(self.company_id, self.login.user_id)

    def set_company_info(self, comp_id):
        data = self.DB.get_all_companies()
        for item in data:
            if item[0] == comp_id:
                self.company_name = item[1]
                self.balance = item[2]

        self.company_id = comp_id

    def get_company(self):
        if not self.__check_users_company(self.login.user_id):
            for company in self.DB.get_all_companies():
                if company[4] == self.login.user_id:
                    return company
        return False


    def add_money(self, amount):
        self.DB.add_company_money(self.login.users_company_id, amount)

    def get_balance(self):
        return self.DB.get_company_balance(self.login.users_company_id)