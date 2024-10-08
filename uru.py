year = int(input())

if year % 4 != 0:
    print(str(year) + "年はうるう年ではない。")
elif year % 100 != 0:
    print(str(year) + "年はうるう年である。")
elif year % 400 != 0:
    print(str(year) + "年はうるう年ではない。")
else:
    print(str(year) + "年はうるう年である。")
