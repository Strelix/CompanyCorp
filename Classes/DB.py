import mariadb


class Database:
    def __init__(self):
        try:
            self.connection = mariadb.connect(user='root',
                                              database='CompanyCorp',
                                              password='',
                                              host='localhost')
            print('Database Connected')
        except mariadb.Error as error_message:
            print(f'DB Error: {error_message}')

    def __execute(self, statement):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            cursor.close()
        except mariadb.Error as error_message:
            print(f'Database Error: {error_message}')

    def __execute_params(self, statement, params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement, params)
            cursor.close()
        except mariadb.Error as error_message:
            print(f'Database Error: {error_message}')

    def __get_execute(self, statement):
        try:
            cursor = self.connection.cursor()
            cursor.execute(statement)
            saved = cursor.fetchall()
            cursor.close()
            return saved

        except mariadb.Error as error_message:
            print(f'Database Error: {error_message}')
            return

    def __get_users(self):
        return self.__get_execute('SELECT * FROM users')

    def get_all_users(self):
        return self.__get_users()

    def __append_user(self, username, pin):
        hashed_pin = pin
        statement = f'INSERT INTO users (username, pin) VALUES (?, ?)'
        self.__execute_params(statement, (username, hashed_pin))

    def get_user_by_id(self):
        print('a')

    def sign_up(self, username, pin):
        print(self.__get_users())
        self.__append_user(username, pin)
        print(self.__get_users())
