# Hvis der skal udskrives hvilken type "Model" skal det gøres således!
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)
print()

# Kan også bruge get
print("Get benyttes")
x = thisdict.get("model")
print(x)
print()

# Nu udskrives nøgleordene for thisdict
print("Nøgleord")
x = thisdict.keys()
print(x)
print()

# Udskrives værdier
print("Værdier udskrives")
x = thisdict.values()
print(x)
print()
