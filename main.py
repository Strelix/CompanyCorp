from Classes.Login import Login
from Classes.Companies import Company
from Classes.DB import Database
from Classes.Files import Files
from getpass import getpass

FILES = Files()
commands = FILES.read_file('commands.json')
displays = FILES.read_file('display.json')
command_list = []
command_action_list = []
command_actions = {}
prefix = '!'

DB = Database()
LOGIN = Login(DB)
COMPANIES = Company(DB, LOGIN)

for command in commands:
    index = commands.index(command)
    command_list.append(command["command"])
    command_action_list.append(command)

quit = False
joined = False
while not quit:
    try:
        if not joined:
            print('Welcome to the game! Use !help to get started. \n')
            joined = True

        user_command = str(input('  >  ')).lower()

        if user_command.replace(prefix, '') in command_list:
            found = False
            for command in commands:
                if not found:
                    current = command_action_list[commands.index(command)]
                    if current['command'] == user_command.replace(prefix, ''):
                        found = True

                        if current['type'] == 'display':
                            print(displays[0][current['action']])

                        if current['command'] == 'login':
                            if not LOGIN.logged_in:
                                username = input('Please enter your username\n     >  ')
                                pin = getpass('Please enter your four digit pin\n     >  ')
                                if len(pin) == 4 and pin.isnumeric():
                                    print(LOGIN.login(username, pin)[1])
                                    COMPANIES.set_company_info(LOGIN.users_company_id)
                                else:
                                    print('Make sure your pin is 4 digits long!')

                        if current['command'] == 'balance':
                            if not LOGIN.logged_in:
                                print('Please login first using !login.')
                                continue

                            print(f'Your companies balance is currently: {COMPANIES.balance}')

    except:
        pass

# LOGIN.login('Trey', '1234')
#
# COMPANIES.remove_money(1)
