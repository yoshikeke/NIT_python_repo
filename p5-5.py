import math
import re
import matplotlib.pyplot as plt
file = "data_sincos.txt"
with open(file) as fileobj:
    num = fileobj.read()
    numlist = re.split("[,\n]",num)



digree = numlist[::3]
arc1 = numlist[1::3]
arc11 = [float(s) for s in arc1]
arc2 = numlist[2::3]
arc22 = [float(s) for s in arc2]

n = int(input())
if n:
    plt.plot(digree,arc22)
else:
    plt.plot(digree,arc11)

plt.show()
