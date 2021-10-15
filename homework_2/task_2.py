list_1 = input('введите элементы списка ').split()
print(list_1)
list_2 = []
j = 0
i = len(list_1) - 1
while j < i:
    list_2.insert(j,list_1[j+1])
    list_2.insert(j+1,list_1[j])
    j += 2
if i % 2 == 0:
    list_2.insert(i,list_1[i])
print(list_2)
