file = "data_exam.csv"

fobj = open(file, "r",encoding="utf_8")

eng  = []
math = []

while True:

    line = fobj.readline()
    aline = line.rstrip()
   

    if aline != "":
        data = aline.split(",")
        eng.append(int(data[0]))
        math.append(int(data[1]))
    else:
        break
fobj.close()
