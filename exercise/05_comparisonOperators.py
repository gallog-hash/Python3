fullname = input("Insert your full name: ")

if len(fullname) < 3:
    print('Name must be at least 3 characters')
elif len(fullname) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print(f'Name looks good! [len = {len(fullname)}]')