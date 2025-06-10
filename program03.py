# To‘g‘ri javob kiritilmaguncha davom et.

print("O'zbekiston poytaxti nima?")

capital = "Toshkent"
answer = ""

while answer != capital:
    answer = input("Javobiz: ").capitalize()
    if answer == capital:
        print("To'g'ri")
    else:
        print("Xato")