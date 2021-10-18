def my_func(x, y):
    i = 1
    j = 1
    while i <= y:
        j *= x
        i += 1
    return 1 / j


x = float(input("число, возводимое в степень "))
y = int(input("степень "))
print(my_func(x, y))
