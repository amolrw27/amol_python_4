import random

letter_abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbol_abc=['!','@','#','$','%','^','*','(',')','+','_']

numbers_abc=['1','2','3','4','5','6','7','8','9','0']


print("Welcome to the PyPassword Generator!")

total_char=int(input("How many total character in your password do you want?\n"))

letter=int(input("How many letters would you like in your password?\n"))

symbol=int(input("How many symbols would you like?\n"))

number=int(input("How many numbers would you like?\n"))

total=int(letter+symbol+number)
if(total_char!=total):
    print("Wrong input")
else:
    password=[]
    for i in range(1, letter + 1):
        password_a=random.choice(letter_abc)
        password+=password_a

    for i in range(1, symbol + 1):
        password_b=random.choice(symbol_abc)
        password+=password_b

    for i in range(1, number + 1):
        password_c=random.choice(numbers_abc)
        password+=password_c

    print(password)
    random.shuffle(password)
    print(password)

    a=""
    for i in password:
        a+=i
    print(a)