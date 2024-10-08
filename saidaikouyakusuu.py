m,n = map(int,input().split())
i = 0

while n != 0 :
    i = m % n
    if i == 0 :
        break
    m = n
    n = i
print("最大公約数は" + str(n) + "です。")
