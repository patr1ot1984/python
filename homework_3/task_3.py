def my_func(num_1, num_2, num_3):
    min_num = min(num_1, num_2, num_3)
    sum_num = num_1 + num_2 + num_3 - min_num
    return sum_num

s_1 = int(input(" первое слогаемое : "))
s_2 = int(input(" второе слогаемое : "))
s_3 = int(input(" третье слогаемое : "))
print(my_func(s_1, s_2, s_3))

