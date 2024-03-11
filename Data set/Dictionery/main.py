# Her oprettes en Dictionary med bil navne.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print()

# Hvis det kun er mærket der skal udskrives!
print("Nu er det kun mærket der udskrives!!")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print()
# der kan ikke være 2 ens i Dictionary!!!
print("Der kan ikke være 2 ens i Dictionary!!!")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print()
# Vil du se havormange elemter der i Dictionaryen, skal len benyttes.
print("Antal elemter i thisdict =", len(thisdict))
print()
# Der kan benyttes alle typer af data
print("Flere typer af data kan benyttes i Dictionary")
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
