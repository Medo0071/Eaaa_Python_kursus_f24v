# ændring af værdier i en Dict
print("Nu ændres årstallet for bilen")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change
print()

# Nu udskrives data parvis
print("Data udskrives parvis!")
x = car.items()
print(x)
print()

# Tilføje et elemnent til Dict
print("Nu tilføjes color til Dict")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change

# Findes nøglen?
print("Undersøger om nøglen findes")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
