from random import randint

number = randint(1, 10)
# print(number) -- # Tekshirib ko'ring

attempt = 0

while attempt < 3:
    answer = int(input("Sonni toping (1-10): "))
    attempt += 1

    if answer == number:
        print("To'g'ri")
        break
    else:
        print("Xato")
        
if answer != number:
    print("Urinishlar tugadi")