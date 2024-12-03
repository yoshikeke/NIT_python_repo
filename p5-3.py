import math
fileR = "degree_data.txt"
fileW = "sin_data.txt"
fileobjW = open(fileW,"w",encoding="utf_8")
with open(fileR) as fileobjR:
    num = fileobjR.read()
    newnum = num.rstrip(".")
    numlist = newnum.split("\n")

for digree in numlist:
    if digree:
        fileobjW.write(digree)
        fileobjW.write(",")
        numsin = math.sin(math.radians(float(digree)))
        numsin = str(numsin)
        fileobjW.write(numsin)
        fileobjW.write("\n")
