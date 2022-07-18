names = ['Federica', 'Giuseppe', 'Franca', 'Eugenio', 'Federica', 'Federica']
uniqueNames = []
for name in names:
    if not(name in uniqueNames):
        uniqueNames.append(name)
print(uniqueNames)

numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
