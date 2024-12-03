file_eng = "data_eng.csv"
file_math = "data_math.csv"
file_out = "data_eng2.csv"

fobj_eng = open(file_eng, "r",encoding="utf_8")
fobj_math = open(file_math, "r",encoding="utf_8")
fobj_out = open(file_out, "w",encoding="utf_8")

while True:

    line = fobj_eng.readline()
    aline = line.rstrip()
    line = fobj_math.readline()
    aline = line.rstrip()

    if aline != "":
        
        fobj_out.write(aline+"\n")
    else:
        break
fobj_eng.close()
fobj_math.close()
fobj_out.close()