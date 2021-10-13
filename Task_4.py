ch = int(input("введите число : "))
max = ch % 10
i = 100
j = 10
while ch // i >= 1:
    a = (ch%i) // j
    i *= 10
    j *= 10
    if a > max:
        max = a
print(max)
