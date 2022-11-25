### IMPORTS ###
from Classes.Login import Login
from Classes.Companies import Company
from Classes.DB import Database
from Classes.Files import Files
from getpass import getpass
## END IMPORTS ##

### SET VARIABLES ###
FILES = Files()
commands = FILES.read_file('commands.json')
displays = FILES.read_file('display.json')[0]
staff_list = FILES.read_file('staff.json')
command_list = []
command_action_list = []
command_actions = {}
prefix = '!'

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

quit = False
joined = False
while not quit:
    # try:
        if not joined:
            print('Welcome to the game! Use !help to get started. \n')
            joined = True

        user_command = str(input('  >  ')).lower().split(' ')
        if user_command[0].replace(prefix, '') in command_list:
            found = False
            for command in commands:
                if not found:
                    current = command_action_list[commands.index(command)]
                    if current['command'] == user_command[0].replace(prefix, ''):
                        found = True

                        if current['type'] == 'display':
                            print(displays[current['action']])

                        if current['command'] == 'login':
                            if not LOGIN.logged_in:
                                username = input('Please enter your username\n     >  ')
                                pin = getpass('Please enter your four digit pin\n     >  ')
                                if len(pin) == 4 and pin.isnumeric():
                                    login_msg = LOGIN.login(username, pin)
                                    if login_msg[0]:
                                        COMPANIES.set_company_info(LOGIN.users_company_id)
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

                                print(LOGIN.signUp(username, pin)[1])

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
                                    if COMPANIES.company_name != None and COMPANIES.company_id != None:
                                        COMPANIES.hire_staff(user_command[1])
                                        amount = COMPANIES.get_staff()[user_command[1]]
                                        print(f'Hired! You now have {amount} {user_command[1]} members.')
                                    else:
                                        print(displays["login"])
                            else:
                                print('You can hire all of these staff:')
                                for name in staff_list[0]:
                                    type = staff_list[0][name]

                                    print(f'{name} - £{format(type["price"], ",.2f")}')


                        if current['command'] == 'staff':
                            if COMPANIES.company_name != None and COMPANIES.company_id != None:
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
                                    print(display['deleted'])
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

                        if current['command'] == 'g':
                            us = DB.get_all_users()
                            print(us, type(us))

                        if current['command'] == 'exit':
                            break

    # except Exception as error:
    #     print(f'[ERROR] {error}')