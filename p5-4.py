import math
import re
import matplotlib.pyplot as plt
file = "sin_data.txt"
with open(file) as fileobj:
    num = fileobj.read()
    numlist = re.split("[,\n]",num)

print(numlist)

digree = numlist[::2]
digree.pop(-1)
arc = numlist[1::2]
float_list = [float(s) for s in arc]

print(numlist)
print(digree)
print(arc)
plt.plot(digree,float_list)
plt.show()
