# 1 donasi 2500 so‘m bo‘lgan mahsulotdan 
# foydalanuvchi 1 tadan 10 tagacha olganida 
# umumiy narxlarni jadval ko‘rinishida chiqaring.

template = "{i} dona = {result}"

price = 2500
stop = int(input("Nechta oldingiz?: "))

if stop > 10 or stop <=0:
    print("Faqat 1 tadan 10 tagacha olish mumkin")

for i in range(1, stop+1):
    result = price*i
    print(template.format(i = i, result = result))