from Classes.Login import Login
from Classes.Companies import Company
from Classes.DB import Database
from Classes.Files import Files

FILES = Files()
commands = FILES.read_file('commands.json')[0]
prefix = '!'

DB = Database()
LOGIN = Login(DB)
COMPANIES = Company(DB, LOGIN)

for ind, item in enumerate(commands):
    print(f'Ind: {ind}, {item}, {[*commands.values()][ind]}')

exit = False
joined = False
while not exit:
    try:
        if not joined:
            print('Welcome to the game! Use !help to get started. \n')
            joined = True

        command = str(input('  >  '))


        if command.replace(prefix, '') in commands:
            print('in')

    except:
        pass

# LOGIN.login('Trey', '1234')
#
# COMPANIES.remove_money(1)
