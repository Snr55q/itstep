from cgi import print_environ_usage

print("Hello World")

name = input("Введіть своє ім'я: ")
age = int(input("Введіть свій вік:"))
print(f"Привіт, {name}, тобі {age} років!")

age1 = int(input("Введіть свій вік: "))

if age1 >= 18:
    print("Вхід дозволено!")

if age1 < 18:
    print("Вхід заборонено!")


import random

secret_num = random.randint(1, 10)

attempts = 0
while attempts < 3:
    guess = int(input("Введи число від 1 до 10: "))
    attempts += 1
    if guess == secret_num:
        print(f"Вітаю, ти вгадав число за {attempts} разів!")

    else:
         print("Нажаль, це не вірно")
    if attempts == 3:
         print("На жаль, ти не вгадав число. Спробуй ще раз!")

fromm = int(input("Введіть перше число: "))
to = int(input("Введіть друге число: "))
print(f"Числа з {fromm} по {to}: ")

for i in range(fromm, to+1):
    print(i)

num = int(input("Введіть число: "))

print("Парні Числа у зворотному порядку: ")
for i in range(num, 0, -1):
    if i % 2 == 0:
        print(i)


def factorial(numb):
    n = 1
    for i in range(1, numb + 1):
        n *= i
    return n

number = int(input("Введіть число: "))

print(f"Факторіал числа {number} = {factorial(number)}")

