def my_generator(finish):
    fact_nums = 1
    for el in range(1, finish + 1):
        fact_nums *= el
        yield fact_nums


finish = int(input("введите целое положительное число : "))
fact = my_generator(finish)
print(fact)
for el in fact:
    print(el)
