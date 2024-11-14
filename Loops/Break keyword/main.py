count = 0

while True:  # Den er altid sand!!
    print(count)
    count += 1
    if count > 5:
        break  # Loopen stoppe hvis count >= 5
        

correct_password = "securepassword"  # Change this to your desired password
user_input = input("Enter your password: ")

while user_input != correct_password:
    print("Incorrect password. Please try again.")
    user_input = input("Enter your password: ")

print("Correct password entered. Access granted!")