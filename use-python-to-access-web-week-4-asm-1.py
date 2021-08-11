import urllib.request
import re
from bs4 import BeautifulSoup
try:
    numbers = list()
    x = urllib.request.urlopen(
        "http://py4e-data.dr-chuck.net/comments_1231479.html")
    soup = BeautifulSoup(x.read(), "html.parser")
    for item in soup.findAll("span"):
        numbers.append(int(re.search("[0-9]+", str(item)).group()))
    print(sum(numbers))
except Exception as e:
    print(str(e))
