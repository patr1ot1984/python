from itertools import count
from itertools import cycle

for el in count(int(input('стартовое число : '))):
    if el > 10:
        break
    else:
        print(el)
i = 0
prog = ["python"]
for el in cycle(prog):
    if i > 10:
        break
    print(el)
    i += 1
