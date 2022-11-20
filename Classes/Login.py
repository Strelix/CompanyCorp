import json
from Classes.DB import Database

class Login:
    def __init__(self):
        self.DB = Database()
        print('Connected')


    def __check_exists(self, username)-> bool:
        taken = False
        users = self.DB.get_all_users()
        print(f'Users: {users}')
        # for user in users:
        #     if user[1] == username:
        #         taken = True

        return taken


    def login(self, username, pin):
        # print(' login ')
        self.DB.get_user_by_id()

    def logout(self):
        print(' logout ')

    def signUp(self, username, pin):
        if self.__check_exists(username):
            return False, 'This username has already been taken.'

        self.DB.sign_up(username, pin)
