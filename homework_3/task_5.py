def my_sum():
    sum = 0
    st = True
    while st is True:
        my_numbers = input("введите чиcла или символ выхода ").split()
        s = 0
        for el in range(len(my_numbers)):
            if my_numbers[el] == 'e':
                st = False
                break
            else:
                s = s + int(my_numbers[el])
        sum = sum + s
        print(f'сумма чисел равна {sum}')
    my_sum()
