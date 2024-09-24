FirstName = input("Enter your first name: ")
LastName = input("Enter your last name: ")
CurrentYear = int(input("Enter the current year: "))
BirthYear = int(input("Enter your birth year: "))

Age = (CurrentYear - BirthYear)
print("Hello", FirstName, LastName, "!")
print("You are ", Age, " years old.")

print("In the next year ", CurrentYear + 1, ", you will be ", Age + 1, " years old.")

print("--------------------------------------")
print("Written by, Valiant Hulsey")




