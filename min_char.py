def min_char_add(password):
    special = any(char in "!@#$%^&*()_+" for char in password)
    digit = 0
    for i in range(len(password)):
        if password[i].isdigit():
            digit = 1

    length = 0
    if len(password) < 6:
        length = 1

    upper = 0
    for i in range(len(password)):
        if password[i].isupper():
            upper = 1

    lower = 0
    for i in range(len(password)):
        if password[i].islower():
            lower = 1

    return 5 - (special + digit + length + lower + upper)


n = input("Enter Password to check: ")
k = min_char_add(n)
print(k)
