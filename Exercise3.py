"""
If the entered password contains: 7, 711, 1111 - true
"""

pwd = list(input("Password: "))

for i in range(len(pwd) - 3):
    if int(pwd[i] + pwd[i + 1] + pwd[i + 2] + pwd[i + 3]) == 1111:
        pwd[i] = '0'
        pwd[i + 1] = '0'
        pwd[i + 2] = '0'
        pwd[i + 3] = '0'
pwd = [x for x in pwd if x != '0']

for i in range(len(pwd) - 2):
    if int(pwd[i] + pwd[i + 1] + pwd[i + 2]) == 711:
        pwd[i] = '0'
        pwd[i + 1] = '0'
        pwd[i + 2] = '0'
pwd = [x for x in pwd if x != '0']

for i in range(len(pwd)):
    if int(pwd[i]) == 7:
        pwd[i] = '0'
pwd = [x for x in pwd if x != '0']

if not pwd:
    print('True')
else:
    print('False')