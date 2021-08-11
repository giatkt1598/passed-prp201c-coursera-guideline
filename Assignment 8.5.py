fh = open("./mbox-short.txt", "r")
count = 0
for line in fh:
    if line.startswith("From "):
        print(str(line).split()[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
