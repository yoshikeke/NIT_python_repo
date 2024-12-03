file_in = "data_eng.csv"
file_out = "data_eng2.csv"

fobj_in = open(file_in, "r",encoding="utf_8")
fobj_out = open(file_out, "w",encoding="utf_8")

while True:
    line = fobj_in.readline()
    aline = line.rstrip()

    if aline != "":
        print(aline)
        fobj_out.write(aline+"\n")
    else:
        break
fobj_in.close()
fobj_out.close()