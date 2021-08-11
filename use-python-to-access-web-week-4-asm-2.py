import urllib.request
import re
from bs4 import BeautifulSoup

# http://py4e-data.dr-chuck.net/known_by_Shaarvin.html
link = input("Enter URL:")
count = int(input("Enter count:"))  # 7
position = int(input("Enter position:"))  # 18

while count >= 0:
    print("Retrieving:", link)
    data = urllib.request.urlopen(link).read().decode()
    soup = BeautifulSoup(data, "html.parser")
    knownPeople = soup.findAll("a")[position - 1]

    urlUser = re.search("http://.*html", str(knownPeople)).group()
    nameUser = BeautifulSoup(str(knownPeople), "html.parser").text
    link = urlUser
    count -= 1
