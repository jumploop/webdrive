from accountDetails import AccountDetail
from fort import Fort

# info = {'firstname': 'Kellen', 'lastname': 'Dorsey', 'sex': 'M', 'ssn': '515-38-2672', 'fathername': 'Deacon',
# 'phone_num': '620-528-8873', 'parent_phone': '620-259-3433'} email = 'helloworld1234@gmail.com' print(info)

print("|==========================|")
print("|                          |")
print("|  PLEASE USE 'USA' VPN    |")
print("|                          |")
print("|                     dydx |")
print("|==========================|")

email = input("Enter your email-id (Do not use fake email) : ")
generate_info = AccountDetail()
info = generate_info.getInfo()
print(info)
fort_page = Fort(info, email)
fort_page.start_process()
