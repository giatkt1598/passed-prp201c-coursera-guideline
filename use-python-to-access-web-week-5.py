from bs4 import BeautifulSoup
import urllib.request

link = input("Enter location: ")
sum = 0
count = 0
print("Retrieving", link)
data = urllib.request.urlopen(link).read().decode()
print("Retrieved", len(data))
soup = BeautifulSoup(data, "xml")
for item in soup.findAll("comment"):
    sum += int(item.count.text)
    count += 1
print("Count:", count)
print("Sum:", sum)
