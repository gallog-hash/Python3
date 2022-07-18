numbers = [0, 9, 87, 65, 344, 12]
largest = numbers[0]
for number in numbers[1:]:
    if number > largest:
        largest = number
print(largest)