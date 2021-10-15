month = int(input(' Введите номер месяца : '))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if winter.count(month) == 1:
    print("зимний месяц")
elif spring.count(month) == 1:
    print("весенний месяц")
elif summer.count(month) == 1:
    print("летний месяц")

else:
    print("осенний месяц")
dict_1 = {
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень",
    12: "зима"
}
print(dict_1.get(month))
