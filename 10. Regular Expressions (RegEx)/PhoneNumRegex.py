import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

print('Write a message: ')
message = input()

print("""Do you want to find the first phone numbers or all phone numbers?
1. First Phone Number
2. All Phone Numbers""")

option = input()

if option == '1':
    mo = phoneNumRegex.search(message)
    print(mo.group())
elif option == '2':
    print(phoneNumRegex.findall(message))
