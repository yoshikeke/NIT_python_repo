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

dataY2 = list(range(len(dataY)))
for i in range(len(dataY)):
    dataY2[i] = 0

for value in range(len(dataY)):
    count = 0
    for i in range(-5,6):
        index = value + i
        if index < 0:
            continue
        elif index >= len(dataY):
            continue
        count += 1
        dataY2[value] += dataY[index]
    dataY2[value] = dataY2[value] / count
plt.plot(dataX,dataY,label="Originail Wave")
plt.plot(dataX,dataY2,label="Moving Average")
plt.legend()
plt.show()

