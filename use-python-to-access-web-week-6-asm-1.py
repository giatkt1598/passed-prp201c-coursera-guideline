import urllib.request
import json

link = input("Enter location: ")
count = 0
sum = 0
print("Retrieving", link)
text = urllib.request.urlopen(link).read().decode()
print("Retrieved", len(text))
data = json.loads(text)
for comment in data["comments"]:
    count += 1
    sum += int(comment["count"])
print("Count:", count)
print("Sum:", sum)
