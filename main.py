### IMPORTS ###
from Classes.Login import Login
from Classes.Companies import Company
from Classes.DB import Database
from Classes.Files import Files
from getpass import getpass
import sys, os

## END IMPORTS ##

### SET VARIABLES ###
FILES = Files()
commands = FILES.read_file('commands.json')
displays = FILES.read_file('display.json')[0]
staff_list = FILES.read_file('staff.json')
command_list = []
command_action_list = []
command_actions = {}
PREFIX = '!'

## END SET VAR ##

### INITIALISE CLASSES ###
DB = Database()
LOGIN = Login(DB)
COMPANIES = LOGIN.COMPANY
## END INITIALISE CLASSES ##

for command in commands:
    index = commands.index(command)
    command_list.append(command["command"])
    command_action_list.append(command)
QUIT = False
JOINED = False
while not QUIT:
    try:
        if not JOINED:
            print('Welcome to the game! Use !help to get started. \n')
            JOINED = True

        user_command = str(input('  >  ')).lower().split(' ')
        if user_command[0].replace(PREFIX, '') in command_list:
            FOUND = False
            for command in commands:
                if not FOUND:
                    current = command_action_list[commands.index(command)]
                    if current['command'] == user_command[0].replace(PREFIX, ''):
                        FOUND = True
                        if current['type'] == 'display':
                            print(displays[current['action']])

                        if current['command'] == 'login':
                            if not LOGIN.logged_in:
                                username = input('Please enter your username\n     >  ')
                                pin = getpass('Please enter your four digit pin\n     >  ')
                                if len(pin) == 4 and pin.isnumeric():
                                    print(1)
                                    login_msg = LOGIN.login(username, pin)
                                    print(2)
                                    if login_msg[0]:  # If login_msg = True not False
                                        print(COMPANIES.set_company_info(LOGIN.users_company_id))
                                        print(3)
                                        print(displays['dashes'])
                                        print(displays['success_login'].format(LOGIN.username))
                                        print(displays['dashes'])
                                    else:
                                        print(login_msg[1])
                                else:
                                    print('Make sure your pin is 4 digits long!')
                            else:
                                print('You\'re already logged in!')

                        if current['command'] == 'signup':
                            if not LOGIN.logged_in:
                                username = input('Please enter a username you\'d like you have\n     >  ')
                                pin = getpass('Please enter a four digit pin\n     >  ')

                                print(LOGIN.sign_up(username, pin)[1])

                        if current['command'] == 'create':
                            if LOGIN.logged_in:
                                try:
                                    if user_command[1]:
                                        name = user_command([1])
                                except:
                                    name = input('Please enter a name for your company\n\n  >  ')

                                print(COMPANIES.create(name)[1])
                            else:
                                print(displays['login'])

                        if current['command'] == 'balance':
                            if not LOGIN.logged_in:
                                print(displays['login'])
                                continue
                            if not COMPANIES.company_name:
                                print(displays['company_needed'])
                                continue

                            print(f'Your companies balance is currently: {COMPANIES.balance}')

                        if current['command'] == 'hire':
                            if len(user_command) > 1:
                                if user_command[1] in staff_list[0]:
                                    if COMPANIES.company_name is not None and COMPANIES.company_id is not None:
                                        return_message = COMPANIES.hire_staff(user_command[1])
                                        amount = COMPANIES.get_staff()[user_command[1]]
                                        if return_message[0]:
                                            print(displays['dashes'])
                                            print(f'Hired! You now have {amount} {user_command[1]} members.')
                                            print(displays['dashes'])

                                        else:
                                            print(return_message[1])
                                    else:
                                        print(displays["login"])
                            else:
                                print('You can hire all of these staff:')
                                for name in staff_list[0]:
                                    department = staff_list[0][name]

                                    print(f'{name} - £{format(department["price"], ",.2f")}')

                        if current['command'] == 'staff':
                            if COMPANIES.company_name is not None and COMPANIES.company_id is not None:
                                print(COMPANIES.get_staff())

                            else:
                                print(displays["login"])

                        if current['command'] == 'logout':
                            if LOGIN.logged_in:
                                print(LOGIN.logout()[1])
                            else:
                                print('You\'re already logged out! Silly.')

                        if current['command'] == 'delete':
                            if LOGIN.logged_in:
                                inp = input('Please type YES if you\'d like to delete your company.\n\n  >  ')

                                if inp.lower() == 'yes':
                                    COMPANIES.delete_company()
                                    print(displays['deleted'])
                                else:
                                    print('Okay! I won\'t delete your company.')
                            else:
                                print(displays['login'])

                        if current['command'] == 'info':
                            if LOGIN.logged_in:
                                info = COMPANIES.get_company_info()
                                print(info)
                                print(f'Your company info:\n--------------\n'
                                      f'NAME: {info["name"]}'
                                      f' ({info["id"]})\n'
                                      f'BALANCE:  £{format(info["balance"], ",.2f")}\n'
                                      f'STAFF: {info["staff"]}')
                            else:
                                print(displays['login'])

                        if current['command'] == 'exit':
                            QUIT = True
                            break

    except Exception:
        # print(f'[ERROR] {error}')
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(f'{exc_type}, {exc_obj}, {exc_tb}. File: {fname}')
