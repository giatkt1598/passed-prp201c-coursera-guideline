fh = open("./mbox-short.txt", "r")
tongSo = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = float(line[line.find("0."):])
    tongSo = tongSo + x
    count = count + 1
print(tongSo / count)
print("Done")
