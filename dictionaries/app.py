customer = {
    "name": "Giuseppe Gallo",
    "age": 32,
    "email": "giuseppe.gallo8790@gmail.com"
}
print(customer["name"])
print(customer.get('age'))
print(customer.get('address'))
print(customer.get('birthdate', 'Jul 8, 1990'))

customer["name"] = "Jack Smith"
print(customer["name"])