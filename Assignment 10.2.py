
# Hello
fh = open("./mbox-short.txt")

result = {}
for line in fh:
    if str(line).startswith("From "):
        time = (str(line).split()[5])
        hour = time[0: 2]
        if (result.get(hour) == None):
            result[hour] = 1
        else:
            result[hour] += 1
result = sorted(result.items(), key=lambda item: item[0])
for item in result:
    print(item[0], item[1])
