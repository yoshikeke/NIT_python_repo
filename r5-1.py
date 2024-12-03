import matplotlib.pyplot as plt
import re
file = "./population.txt"
data = []
column = []
city_data = []
with open(file,"r",encoding="utf_8") as fileobj:
    city_data = fileobj.read()
    data = re.split("[,\n]",city_data)

print(data[15::15])
plt.plot(data[15::15],data[16::15])
plt.show()
    