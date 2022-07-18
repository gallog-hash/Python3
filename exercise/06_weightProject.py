weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    print(f'You are {0.45359237 * weight} kg')
elif unit.upper() == 'K':
    print(f'You are {2.204623 * weight} pounds')
else: 
    print("You entered an incorrect unit!")
    print("Please, try to run the code again :)")