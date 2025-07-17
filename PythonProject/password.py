import random
import string

print("******** Password Generator ********")
length = int(input("Enter Password Length: "))

all_charc = string.digits + string.ascii_letters + string.punctuation
password = []

if length < 8:
    print("Password Length must be 8 characters long")
else:
    for a in range(length):
        password.append(random.choice(all_charc))

    random.shuffle(password)
    string_pswd = "".join(password)
    print(f"Randomly Generated Password is: {string_pswd}")