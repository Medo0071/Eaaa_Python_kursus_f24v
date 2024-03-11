print("1) læg to tal sammen")
print("2) Gange to tal")
print("3) Træk to tal fra hinanden")
print("4) stop")
menutal = int(input("Tast 1, 2, 3 eller 4"))

while True:
    if menutal == 1:  # Læg to tal sammen
        print("To tal skal lægges sammen!")
        tal1 = int(input("Første tal"))
        tal2 = int(input("Andet tal"))
        print(tal1 + tal2)
        print("1) læg to tal sammen")
        print("2) Gange to tal")
        print("3) Træk to tal fra hinanden")
        print("4) stop")
        menutal = int(input("Tast 1, 2, 3 eller 4"))
        # Tilføj menuen
    elif menutal == 2:
        print("To tal ganges")
        tal1 = int(input("Første tal"))
        tal2 = int(input("Andet tal"))
        print(tal1 * tal2)
        print("1) læg to tal sammen")
        print("2) Gange to tal")
        print("3) Træk to tal fra hinanden")
        print("4) stop")
        menutal = int(input("Tast 1, 2, 3 eller 4"))

    elif menutal == 3:  # Træk to tal fra hinanden
        print("To tal trækkes fra hinanden")
        tal1 = int(input("Første tal"))
        tal2 = int(input("Andet tal"))
        print(tal1 - tal2)
        print("1) læg to tal sammen")
        print("2) Gange to tal")
        print("3) Træk to tal fra hinanden")
        print("4) stop")
        menutal = int(input("Tast 1, 2, 3 eller 4"))

    elif menutal == 4:  # Stop programmet
        exit(0)
