
filename = "answersData.csv"
data = []
with open(filename) as dataFile:
    for li in dataFile.readlines():
        li = li.replace("\n", "")
        word, value = li.split(", ")
        value = int(value)
        data.append((word, value))

numlen = max([len(str(v)) for _, v in data])
data.sort(key=lambda x : x[1])
line = ""
i = 0
for w, v in data:
    i += 1
    line += ("{0} : {1:>" + str(numlen) + "}").format(w, v)
    if i == 8:
        print(line)
        line = ""
        i = 0
    else:
        line += " | "