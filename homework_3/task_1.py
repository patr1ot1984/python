def div_num(num_1, num_2):
    if num_2 == 0:
        return print("Error")
    else:
        result = num_1 / num_2
        return result
num_1 = float(input("введите делимое : "))
num_2 = float(input("введите делитель : "))
print(div_num(num_1, num_2))
