import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to Py password generator\n")
nr_letters = int(input("How many letters would you like to add ? "))
nr_numbers = int(input("How many numbers would you like to add ? "))
nr_symbols = int(input("How many symbols would you like to add ? "))
letters_selected = []
numbers_selected = []
symbols_selected = []
for i in range(nr_letters):
    let = random.choice(letters)
    letters_selected.append(let)
for k in range(nr_numbers):
    set = random.choice(numbers)
    numbers_selected.append(set)
for k in range(nr_symbols):
    sym = random.choice(symbols)
    symbols_selected.append(sym)

password = letters_selected+numbers_selected+symbols_selected
passsword = random.shuffle(password)
password = "".join(password)

print(password)


