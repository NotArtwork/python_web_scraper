from bs4 import BeautifulSoup

with open("/main.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

print(doc.prettify)