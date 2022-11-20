from Classes.Login import Login
from Classes.Companies import Company
from Classes.DB import Database

DB = Database()
LOGIN = Login(DB)
COMPANIES = Company(DB, LOGIN)

print(LOGIN.login('Trey', '1234'))



# if LOGIN.logged_in and LOGIN.users_company_id == None:
#     COMPANIES.create('Comp')

# print(COMPANIES.get_company())

print(COMPANIES.get_balance())
print(COMPANIES.add_money(100))
print(COMPANIES.get_balance())