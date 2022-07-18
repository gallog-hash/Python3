def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print('Start')
greet_user(last_name="Messina",first_name="Federica")
greet_user("Giuseppe",last_name="Gallo") # keyword arguments goes after positional arguments
print('Finish')