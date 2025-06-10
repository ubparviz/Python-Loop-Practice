# # 1 dan 5 gacha bo‘lgan sonlar va ularning kvadratlarini ekranga chiqaring. Misol: 1^2 = 1, 2^2 = 4, ...

template = "{i}^2 = {result}"

for i in range(1, 6):
    result = pow(i, 2)
    print(template.format(i = i, result = result))


"yoki siz xoxlagan songacha"

# template = "{i}^2 = {result}"

# stop = int(input("Son kiriting: "))

# for i in range(1, stop+1):
#     result = pow(i, 2)
#     print(template.format(i = i, result = result))