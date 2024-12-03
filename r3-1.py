import re
import matplotlib.pyplot as plt
n = int(input())
processed_data = []
file = "./Brainwave_14ch_128Hz_AU.txt"
with open(file) as fileobj:
    text = fileobj.read()
    newdata = text.rstrip('.')
    data = re.split("[,\n]",newdata)
for i in range(15):
    processed_data.append(data[i::15])
dataX = []
dataY = []
for value in processed_data[0][2:]:
    dataX.append(float(value))
for value in processed_data[n][2:]:
    dataY.append(float(value))
plt.xlabel(processed_data[0][0])
plt.ylabel(processed_data[n][0])
plt.plot(dataX,dataY)
plt.show()

