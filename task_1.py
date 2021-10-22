from sys import argv

name, time, salary, bonus = argv
time = int(argv[1])
rate = float(argv[2])
bonus = int(argv[3])
res = time * rate + bonus
print(res)
