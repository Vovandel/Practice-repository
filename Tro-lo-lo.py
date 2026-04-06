#6.1
s1 = "Hello, World!"
print(s1[0], s1[-1], s1[7:], sep = "\n")

#6.2
s2 = input("Введите строку:")
if len(s2) % 2 == 0:
    print(s2.upper())
else:
    print(s2.lower())

#6.3
s3 = input("Введите строку на английском:")
count_1, count_2 = 0, 0
for char in s3:
    if char in "aeiou":
        count_1 += 1
    elif char in "AEIOU":
        count_2 += 1
print("Заглавных гласных: {}, прописных гласных: {}".format(count_2, count_1))

#6.4
s4 = input("Введите строку:")
result = s4[0]
for i in range(1, len(s4)):
    if s4[i] != s4[i-1]:
        result += s4[i]
print(result)

#6.5
s5, s6 = input("Введите первое слово: "), input("Введите второе слово: ")
if sorted(s5) == sorted(s6):
    print(True)
else:
    print(False)