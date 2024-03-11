# Dette indeholder kommandoer til manipolere lister
# "append" skriver et emne til listen

# opretter tom liste
navne_liste = []
navn = input("Indtast navn1!")
navne_liste.append(navn)
navn = input("Indtast navn2!")
navne_liste.append(navn)
navn = input("Indtast navn3!")
# navn lægges ind i navneliste
navne_liste.append(navn)

print("Navnelisten indeholder", navne_liste)

# Kommandoen "insert" kan placere et emne på en bestemt plads i listen
# Husk at det første element i en liste har placeringen 0!!
tal_liste = [1, 2, 4, 5, 6]
print(tal_liste)
# Nu skal tallet 3 placeres det rigtige sted i listen
tal_liste.insert(2, 3)
print("Tallet 3 placeres på sin plads")
print(tal_liste)
# Tallet 7 skal være sidst
tal_liste.insert(6, 7)
print("Tallet 7 placeres på sin plads")
print(tal_liste)

# Metoden "sort" sortere elementerne i listen
tal_liste2 = [1, 6, 3, 5, 2, 4]
print("Usorteret", tal_liste2)
tal_liste2.sort()
print("Sorteret", tal_liste2)

# Metoden "remove" fjerner et element fra listen
navne_liste2 = ["Lasse", "Hans", "Thomas"]
print(navne_liste2)
navne_liste2.remove("Hans")
# Navnet er fjernet fra listen
print("Hans er væk fra listen nu(remove)!!!", navne_liste2)

# Metoden "pop" fjerner et element fra listen, men vedhjælp af index
navne_liste2 = ["Lasse", "Hans", "Thomas"]
print(navne_liste2)
navne_liste2.pop(1)
# Navnet er fjernet fra listen
print("Hans er væk fra listen nu(pop)!!!", navne_liste2)
