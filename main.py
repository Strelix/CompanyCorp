from Classes.Login import Login
from Classes.Companies import Company
from Classes.DB import Database
from Classes.Files import Files
from getpass import getpass

FILES = Files()
commands = FILES.read_file('commands.json')
displays = FILES.read_file('display.json')
staff_list = FILES.read_file('staff.json')
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

        user_command = str(input('  >  ')).lower().split(' ')
        if user_command[0].replace(prefix, '') in command_list:
            found = False
            for command in commands:
                if not found:
                    current = command_action_list[commands.index(command)]
                    if current['command'] == user_command[0].replace(prefix, ''):
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


                        if current['command'] == 'hire':
                            if len(user_command) > 1:
                                if user_command[1] in staff_list[0]:
                                    if COMPANIES.company_name != None and COMPANIES.company_id != None:
                                        COMPANIES.hire_staff(user_command[1])
                                        amount = COMPANIES.get_staff()[user_command[1]]
                                        print(f'Hired! You now have {amount} {user_command[1]} members.')
                                    else:
                                        print(displays[0]["login"])
                            else:
                                print('You can hire all of these staff:')
                                for name in staff_list[0]:
                                    type = staff_list[0][name]

                                    print(f'{name} - £{format(type["price"], ",.2f")}')


                        if current['command'] == 'staff':
                            if COMPANIES.company_name != None and COMPANIES.company_id != None:
                                print(COMPANIES.get_staff())

                            else:
                                print(displays[0]["login"])

    except:
        pass

# LOGIN.login('Trey', '1234')
#
# COMPANIES.remove_money(1)
