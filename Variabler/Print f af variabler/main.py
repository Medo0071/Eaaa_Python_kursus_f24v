# Udskrift af variabler
a = 3
b = 4

print(f"De to tal er {a} og {b}")
# F string kan også lægge sammen
print(f"a + b = {a + b}")
# Udskrivning af strings
navn = "Lasse"
navn2 = "Hanne"

print(f"De to navne er {navn} og {navn2}")

# Udskrivning af tal både integer
tal = 13234
tal2 = 123123456456

print(f"tal = {tal} og tal2 = {tal2:,}")  # der bliver indsat et komma i tallet tal2 så det er nemmere at læse.
print()
# Udskrivning af float tal

tal3 = 123123.956757

print(f"Jeg vil kun se 2 decimaler af tal3 = {tal3:.2f}")
print(f"Jeg vil kun se 0 decimaler af tal3 = {tal3:.0f}")
print(f"Jeg vil kun se 2 decimaler af tal3 og komma ved 1000 = {tal3:,.2f}")
print()
# Placering af tekst på skærmen

# Jeg bruger variablen navn igen
print(f"Navn bliver placeret indenfor de næste 20 tegn sidst {navn:>20}.")
print(f"Navn bliver placeret indenfor de næste 20 tegn først {navn:20}.")
print(f"Navn bliver placeret indenfor de næste 20 tegn i midten {navn:^20}.")
# Nu bliver der indsat fyld i de 20 tegn
print()
print(f"{navn:_>20}.")
print(f"{navn:*<20}.")
print(f"{navn:-^20}.")

