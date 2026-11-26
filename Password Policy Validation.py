password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")

    if len(password) < 8:
        print("Minimum 8 characters required")
    if not upper:
        print("Uppercase letter required")
    if not lower:
        print("Lowercase letter required")
    if not digit:
        print("Number required")
    if not special:
        print("Special character required")