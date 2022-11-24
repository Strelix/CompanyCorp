import json

import mariadb


class Database:
    def __init__(self):
        try:
            self.connection = mariadb.connect(user='root',
                                              database='companycorp',
                                              password='',
                                              host='localhost')
            print('[SERVER] Database Connected')
        except mariadb.Error as error_message:
            print(f'DB Error: {error_message}')

    def __execute(self, statement):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            self.connection.commit()
            cursor.close()
        except mariadb.Error as error_message:
            print(f'[SERVER] Database Error: {error_message}')

    def __execute_params(self, statement, *params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement, params)
            self.connection.commit()
            cursor.close()
        except mariadb.Error as error_message:
            print(f'[SERVER] Database Error: {error_message}')

    def __get_execute(self, statement):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            saved = cursor.fetchall()
            cursor.close()
            return saved

        except mariadb.Error as error_message:
            print(f'[SERVER] Database Error: {error_message}')
            return

    def __get_users(self):
        return self.__get_execute('SELECT * FROM users')

    def get_all_users(self):
        return self.__get_users()

    def get_all_companies(self):
        return self.__get_execute('SELECT * FROM companies')

    def append_user(self, username, pin):
        hashed_pin = pin
        statement = 'INSERT INTO users (username, pin) VALUES (?, ?)'
        self.__execute_params(statement, username, pin)

    def create_company(self, name, owner_id):
        statement = 'INSERT INTO companies (name, owner_id, staff) VALUES (?, ?, ?)'
        self.__execute_params(statement, name, owner_id, '{"hr": 0, "hacker": 0, "spy": 0}')
        return

    def add_company_to_user(self, company_id, user_id):
        self.__execute(f'UPDATE `users` SET company_id = {company_id} WHERE id={user_id}')

    def add_company_money(self, company_id, amount):
        current = self.__get_execute(f'SELECT * FROM companies WHERE id = {company_id}')
        current = current[0][1]
        total = int(current) + int(amount)
        self.__execute(f'UPDATE companies set balance = {total} WHERE id = {company_id}')

    def remove_company_money(self, company_id, amount):
        current = self.__get_execute(f'SELECT * FROM companies WHERE id = {company_id}')
        current = current[0][2]
        total = int(current) - int(amount)
        self.__execute(f'UPDATE companies set balance = {total} WHERE id = {company_id}')

    def get_company_balance(self, company_id):
        return self.__get_execute(f'SELECT * FROM companies WHERE id = {company_id}')[0][2]

    def save_company(self, company_id, balance, staff, owner_id):
        staff = str(staff)
        # print(f'UPDATE companies SET balance = {balance}, staff = {staff} WHERE company_id = {company_id} AND owner_id = {owner_id};')
        self.__execute_params(
            f'UPDATE companies SET balance = ?, staff = ? WHERE id = ? AND owner_id = ?;', balance, staff, company_id, owner_id)




    # TODO: v
    def get_user_by_id(self):
        print('a')
