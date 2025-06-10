# Maxfiy kodni topish o‘yini

from random import randint

number = randint(100, 999)
print(number) # Tekshirib ko'ring


user_number = int(input("3 xonali maxfiy kodni toping: "))

while user_number != number:
    print("Xato")
    user_number = int(input("Yana urinib ko'ring: "))

print("To'g'ri")