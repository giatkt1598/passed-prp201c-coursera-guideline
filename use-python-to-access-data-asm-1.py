import re

text = open("./regex_sum_1231477.txt", "r").read()

x = re.findall("[0-9]+", text)
listInt = list()
for item in x:
    listInt.append(int(item))
print(sum(listInt))
