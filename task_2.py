sec = int(input("введите число"))
hh = sec // 3600
mm = (sec % 3600) // 60
ss = sec % 60
time = f"{hh:02}:{mm:02}:{ss:02}"
print(time)
