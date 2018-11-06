# Give me u'r birthday date i will tell u how old are u .
import datetime
date = datetime.date.today()
while True:
    print("Enter 'bd' to check old")
    print("Enter 'quit' to end the program .")
    user_input = input(":")

    if user_input == "quit":
     break
    elif user_input == "bd":
        num1 = float(input("Enter year of birth:"))
        print(date.year - num1, "Years")
    else:
        print("Unknown input")

