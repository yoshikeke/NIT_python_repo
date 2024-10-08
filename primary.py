num = int(input())
for i in range(2,num) :
    if num % (i) == 0:
        print("素数ではない")
        exit()
print("素数である")