a = int(input("Введите трёхзначное число: "))
print(f" а) колличество единиц: {a % 10}")
print(f" б) колличество десятков {(a // 10) % 10}")
b = (a // 100) + ((a // 10) % 10) + (a % 10)
print(f" в) суума цифр {b}")
c = (a // 100) * ((a // 10) % 10) * (a % 10)
print(f" г) произведение цифр {c}")
