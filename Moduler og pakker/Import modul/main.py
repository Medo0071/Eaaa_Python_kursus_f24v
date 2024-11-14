menu = print("menu")

mulighed = input("vælg en mulighed (PLUS, MINUS, GANGE, DIVIDERE): ")

num1 = input("number1")
num2 = input("number2")

plus = mulighed == "PLUS"
minus = mulighed == "MINUS"
gange = mulighed == "GANGE"
dividere = mulighed == "DIVIDERE"

if plus:
    num1 = int(input("Indtast første tal: "))
    num2 = int(input("Indtast andet tal: "))
    print(num1 + num2)

elif minus:
    num1 = int(input("indtast første tal:"))
    num2 = int(input("indtast andet tal: "))

elif gange:
    num1 = int(input("indtaste første tal: "))
    num2 = int(input("indtaste andet tal: "))

elif dividere:
    num1 = int(input("indtast første tal: "))
    num2 = int(input("indtast andet tal: "))
