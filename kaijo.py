num = int(input())
kaijo = 1
for i in range(num):
    kaijo *= i + 1
print("n=" + str(num) + ",n!=" + str(kaijo))