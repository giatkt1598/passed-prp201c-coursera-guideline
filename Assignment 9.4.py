fh = open("./mbox-short.txt", "r")
list = list()
for line in fh:
    if line.startswith("From "):
        list.append(str(line).split()[1])
maxEmail = ""
maxNumber = 0
for e in list:
    c = list.count(e)
    if c > maxNumber:
        maxNumber = c
        maxEmail = e
print(maxEmail, maxNumber)
