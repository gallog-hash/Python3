numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    print('x' * x_count) # cheat' solution
print('')

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
print('')

numbers = [2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)