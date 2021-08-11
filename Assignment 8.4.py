fh = open("./romeo.txt", "r")
lst = list()

for line in fh:
    for word in line.strip().split():
        if word not in lst:
            lst.append(word)
print(sorted(lst))
