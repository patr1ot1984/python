my_list = [9, 8, 6, 3, 3, 1]
r = int(input("введите число "))
i = 0
if r > my_list[0]:
    my_list.insert(0,r)
if r == 1:
    my_list.append(r)
else:
    while  my_list[i] >= r:
        if r == my_list[i]:
            j = my_list.count(r)
            my_list.insert(i+j,r)
            break
        i += 1
    my_list.insert(i,r)
print(my_list)
