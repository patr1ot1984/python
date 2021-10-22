my_list = [3, 13, 8, 84, 89, 16]
new_list = [my_list[i] for i in range(1, (len(my_list)-1)) if my_list[i] > my_list[i - 1]]
print(new_list)
