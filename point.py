point = int(input())
sum = 0
count = 0
while point >= 0 :
    sum += point 
    point = int(input())
    count += 1
print("合計値：" + str(sum) + ",平均値：" + str(sum/count))    