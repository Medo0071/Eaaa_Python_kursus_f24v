# Lav en funktion hvor du indtaster de 2 kateter i en retvinklet trekant
# og regner de hypotenusen ud.
# Du skal kunne foretage lige så mange indtastning som du har lyst til!
import math


def hyp(x, y):
    hypotenusen = math.sqrt(x ** 2 + y ** 2)
    print(f"Hypotenusen = {hypotenusen}")


ka1 = int(input("Indtast den første katete? "))
ka2 = int(input("Indtast den anden katete? "))
#Skriv et funktionskald som sender ka1 og ka2 over i hyp funktionen
